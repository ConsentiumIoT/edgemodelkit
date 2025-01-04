# EdgeStream: Sensor Data Acquisition and Logging Library

EdgeStream is a Python library developed by **EdgeNeuron**, designed for seamless sensor data acquisition, real-time processing, and efficient logging. This library bridges the gap between IoT devices and data processing pipelines, making it ideal for edge computing and machine learning applications.

---

## Features

- **Serial Communication**: Supports data acquisition over serial ports.
- **Flexible Data Handling**: Retrieve sensor data as Python lists or NumPy arrays.
- **Real-Time Logging**: Log sensor data into CSV files with optional timestamps and counters.
- **Machine Learning Ready**: Easily integrate with TensorFlow for on-device or server-side inference.

---

## Installation

```bash
pip install edgemodelkit
```

---

## Quick Start

### 1. Initialize the DataFetcher

```python
from edgemodelkit import DataFetcher

# Initialize the DataFetcher with your serial port and baud rate
fetcher = DataFetcher(serial_port="/dev/ttyUSB0", serial_baud=9600)
```

### 2. Fetch Sensor Data

```python
# Get data as a Python list
sensor_data = fetcher.get_data()
print("Sensor Data:", sensor_data)

# Get data as a NumPy array
sensor_data_numpy = fetcher.get_data(return_numpy=True)
print("Sensor Data (NumPy):", sensor_data_numpy)
```

### 3. Log Data to CSV

```python
# Log 10 samples to a CSV file with timestamp and count columns
fetcher.log_data(samples=10, include_timestamp=True, include_count=True)
```

---

## Example: Real-Time Data Processing

```python
from edgemodelkit import DataFetcher

fetcher = DataFetcher(serial_port="/dev/ttyUSB0", serial_baud=9600)

while True:
    # Get data as NumPy array
    sensor_data = fetcher.get_data(return_numpy=True)
    print("Received Data:", sensor_data)

    # Perform some processing (e.g., apply a TensorFlow model)
    # prediction = model.predict(sensor_data)
    # print("Prediction:", prediction)
```

---

## CSV Logging Details

The CSV file is named based on the sensor name (e.g., `IMU_data_log.csv`) and contains:

- **Timestamp**: (Optional) Current time when the data was logged.
- **Count**: (Optional) Incremental counter for the sample.
- **Data Columns**: Each element in the sensor data array is stored in separate columns (e.g., `data_1`, `data_2`, ...).

---

## Dependencies

EdgeStream requires the following Python packages:

- `numpy`
- `pandas`
- `pyserial`
- `tensorflow` (optional for machine learning integrations)

Install dependencies with:

```bash
pip install numpy pandas pyserial tensorflow
```

---

## Contributing

We welcome contributions to EdgeStream! Feel free to submit bug reports, feature requests, or pull requests on our [GitHub repository](https://github.com/EdgeNeuron/edgestream-py).

---

## License

EdgeStream is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For support and inquiries, reach out to us at **support@edgeneuron.ai** or visit our [GitHub repository](https://github.com/EdgeNeuron/edgestream-py).

---

## About EdgeNeuron

EdgeNeuron is a leader in edge computing solutions, empowering developers to create intelligent IoT applications with cutting-edge tools and libraries. Learn more at [edgeneuron.ai](https://edgeneuron.ai).
