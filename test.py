from EdgeStream import DataFetcher

en = DataFetcher(serial_port="/dev/cu.usbserial-0001", serial_baud=9600)
while True:
    sensor_data = en.getData(return_numpy=True)

    print(sensor_data)
