from edgemodelkit import DataFetcher
import matplotlib.pyplot as plt

data_fetcher = DataFetcher(serial_port="/dev/cu.usbserial-0001", baud_rate=115200)

# data_fetcher.log_sensor_data(class_label="hand", num_samples=10, add_timestamp=False, add_count=True)

while True:
    plt.clf()
    sensor_data_numpy = data_fetcher.fetch_data(return_as_numpy=True).reshape(8,8)
    plt.imshow(sensor_data_numpy)
    plt.pause(1)