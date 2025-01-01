import serial
import time
import numpy as np
import pandas as pd
import json
import tensorflow as tf


class DataFetcher:
    def __init__(self, serial_port, baud_rate):
        self.serial_connection = None
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.serial_connection = serial.Serial(port=self.serial_port, baudrate=self.baud_rate)

    def fetch_data(self, return_as_numpy=False):
        """
        Fetches data from the serial port.

        Args:
        - return_as_numpy (bool): Whether to return data as a numpy array.

        Returns:
        - list or numpy array of sensor values.
        """
        raw_packet = json.loads(self.serial_connection.readline().decode())
        if return_as_numpy:
            return np.array(raw_packet['sensorValues'])
        else:
            return raw_packet['sensorValues']

    def log_sensor_data(self, num_samples=5, add_timestamp=True, add_count=True):
        """
        Logs sensor data to a CSV file.

        Args:
        - num_samples (int): Number of data samples to log.
        - add_timestamp (bool): Whether to include a timestamp column.
        - add_count (bool): Whether to include a count column.
        """
        # Read the first data packet to determine the file name
        initial_packet = json.loads(self.serial_connection.readline().decode())
        sensor_name = initial_packet.get("sensorName", "Unknown")
        output_file_name = f"{sensor_name}_data_log.csv"

        # Initialize an empty list to store sensor data
        sensor_data_records = []

        # Process the first packet
        self._process_packet(initial_packet, sensor_data_records, sample_index=0,
                             add_timestamp=add_timestamp, add_count=add_count)

        # Process remaining packets
        for sample_index in range(1, num_samples):
            raw_packet = json.loads(self.serial_connection.readline().decode())
            self._process_packet(raw_packet, sensor_data_records, sample_index,
                                 add_timestamp=add_timestamp, add_count=add_count)

        # Create a DataFrame from the records
        data_frame = pd.DataFrame(sensor_data_records)

        # Write the DataFrame to a CSV file
        data_frame.to_csv(output_file_name, index=False)
        print(f"Data saved to {output_file_name}")

    def _process_packet(self, raw_packet, sensor_data_records, sample_index, add_timestamp, add_count):
        """
        Processes a single data packet and appends it to the records list.

        Args:
        - raw_packet (dict): The incoming data packet.
        - sensor_data_records (list): The list of processed sensor data records.
        - sample_index (int): The current sample index.
        - add_timestamp (bool): Whether to include a timestamp column.
        - add_count (bool): Whether to include a count column.
        """
        # Extract sensor values list
        sensor_values = raw_packet.get("sensorValues", [])

        # Prepare the record dictionary
        sensor_record = {}
        if add_timestamp:
            sensor_record["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
        if add_count:
            sensor_record["sample_count"] = sample_index + 1
        sensor_record.update({f"data_value_{i + 1}": value for i, value in enumerate(sensor_values)})

        # Append the record to the list
        sensor_data_records.append(sensor_record)
