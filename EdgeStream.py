import serial
import time
import numpy as np
import pandas as pd
import json
import tensorflow as tf


class DataFetcher:
    def __init__(self, serial_port, serial_baud):
        self.ser = None
        self.__serial_port = serial_port
        self.__serial_baud = serial_baud
        self.ser = serial.Serial(port=self.__serial_port, baudrate=self.__serial_baud)

    def getData(self, return_numpy=False):
        """
        Fetches data from the serial port.

        Args:
        - data_format (str): Format to return the data. Options: "list", "numpy".

        Returns:
        - list or numpy array of data.
        """
        data_packet = json.loads(self.ser.readline().decode())
        if return_numpy:
            return np.array(data_packet['sensorValues'])
        else:
            return data_packet['sensorValues']

    def logData(self, samples=5, include_timestamp=True, include_count=True):
        """
        Logs sensor data to a CSV file.

        Args:
        - samples (int): Number of data samples to log.
        - include_timestamp (bool): Whether to include a timestamp column.
        - include_count (bool): Whether to include a count column.
        """
        # Read the first data packet to determine the file name
        first_packet = json.loads(self.ser.readline().decode())
        sensor_name = first_packet.get("sensorName", "Unknown")
        file_name = f"{sensor_name}_data_log.csv"

        # Initialize an empty list to store data
        data_records = []

        # Process the first packet
        self._process_packet(first_packet, data_records, count=0, include_timestamp=include_timestamp,
                             include_count=include_count)

        # Process remaining packets
        for count in range(1, samples):
            data_packet = json.loads(self.ser.readline().decode())
            self._process_packet(data_packet, data_records, count, include_timestamp=include_timestamp,
                                 include_count=include_count)

        # Create a DataFrame from the records
        df = pd.DataFrame(data_records)

        # Write the DataFrame to a CSV file
        df.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")

    def _process_packet(self, data_packet, data_records, count, include_timestamp, include_count):
        """
        Processes a single data packet and appends it to the records list.

        Args:
        - data_packet (dict): The incoming data packet.
        - data_records (list): The list of processed records.
        - count (int): The current sample count.
        - include_timestamp (bool): Whether to include a timestamp column.
        - include_count (bool): Whether to include a count column.
        """
        # Extract data list
        data_list = data_packet.get("sensorValues", [])

        # Prepare the row dictionary
        record = {}
        if include_timestamp:
            record["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
        if include_count:
            record["count"] = count + 1
        record.update({f"data_{i + 1}": data for i, data in enumerate(data_list)})

        # Append the record to the list
        data_records.append(record)
