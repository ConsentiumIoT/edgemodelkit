from edgemodelkit import DataFetcher

# Initialize DataFetcher with the appropriate serial port and baud rate
data_fetcher = DataFetcher(serial_port="/dev/cu.usbserial-0001", baud_rate=9600)

# Test fetching data as a numpy array and as a list
print("Testing data fetch:")
sensor_data_numpy = data_fetcher.fetch_data(return_as_numpy=True)
print(f"Data (Numpy Array): {sensor_data_numpy} with shape {sensor_data_numpy.shape}")

data_fetcher.log_sensor_data(class_label=1, num_samples=6, add_timestamp=False, add_count=False)

# sensor_data_list = data_fetcher.fetch_data(return_as_numpy=False)
# print(f"Data (List): {sensor_data_list}")
#
# # Log sensor data to a CSV file with user-defined configurations
# print("\nTesting logging data to CSV:")
# try:
#     num_samples = int(input("Enter the number of samples to log: "))
#     add_timestamp = input("Include timestamp? (yes/no): ").strip().lower() == "yes"
#     add_count = input("Include count? (yes/no): ").strip().lower() == "yes"
#
#     print("Logging data...")
#     data_fetcher.log_sensor_data(num_samples=num_samples, add_timestamp=add_timestamp, add_count=add_count)
#     print("Data logging completed successfully!")
# except Exception as e:
#     print(f"An error occurred while logging data: {e}")
#
# # Continuous fetching demonstration
# print("\nTesting continuous data fetching:")
# try:
#     print("Press Ctrl+C to stop.")
#     while True:
#         sensor_data = data_fetcher.fetch_data(return_as_numpy=True)
#         print(sensor_data)
# except KeyboardInterrupt:
#     print("\nContinuous data fetching stopped.")

