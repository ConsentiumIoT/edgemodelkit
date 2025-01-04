import serial
import time
import numpy as np
import pandas as pd
import json
import os
import sys


def _process_packet(raw_packet, sensor_data_records, sample_index, add_timestamp, add_count):
    sensor_values = raw_packet.get("sensorValues", [])
    sensor_record = {}
    if add_timestamp:
        sensor_record["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    if add_count:
        sensor_record["sample_count"] = sample_index + 1
    sensor_record.update({f"data_value_{i + 1}": value for i, value in enumerate(sensor_values)})
    sensor_data_records.append(sensor_record)


class DataFetcher:
    def __init__(self, serial_port, baud_rate=9600):
        self.serial_connection = serial.Serial(port=serial_port, baudrate=baud_rate)

    @staticmethod
    def ensure_directory_exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    def close_connection(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed.")

    def fetch_data(self, return_as_numpy=False):
        try:
            raw_packet = json.loads(self.serial_connection.readline().decode())
            if return_as_numpy:
                return np.array(raw_packet['sensorValues'])
            else:
                return raw_packet['sensorValues']
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error fetching data: {e}")
            return [] if not return_as_numpy else np.array([])

    def log_sensor_data(self, class_label=None, num_samples=5, add_timestamp=True, add_count=True, output_dir="."):
        initial_packet = json.loads(self.serial_connection.readline().decode())
        sensor_name = initial_packet.get("sensorName", "Unknown")
        file_name = f"{sensor_name}_data_log.csv"
        if class_label:
            directory_path = os.path.join("Dataset", str(class_label))
        else:
            directory_path = "Dataset"

        # Ensure the directory exists
        self.ensure_directory_exists(directory_path)

        # Construct the full file path
        output_file_name = os.path.join(directory_path, file_name)

        sensor_data_records = []
        _process_packet(initial_packet, sensor_data_records, sample_index=0, add_timestamp=add_timestamp, add_count=add_count)

        print(f"Sampling {sensor_name} sensor.")
        for sample_index in range(1, num_samples):
            raw_packet = json.loads(self.serial_connection.readline().decode())
            _process_packet(raw_packet, sensor_data_records, sample_index, add_timestamp=add_timestamp, add_count=add_count)
            sys.stdout.write(f"\rGathering data: {sample_index + 1}/{num_samples}")
            sys.stdout.flush()
        print("\n")

        data_frame = pd.DataFrame(sensor_data_records)
        data_frame.to_csv(output_file_name, index=False)
        print(f"Data saved to {output_file_name}")
