title = ["Time", "Date", "Temperature"]

with open("2022-05-11.csv", "w", newline="") as xlsxfile:
    xlsxwriter = Xlsx.writer(xlsxfile)
    xlsxwriter.writerow(title)

while True:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        serial = serialPort.read(2)  # We used serialPort.read(2) to read only first two characters

        data = serial.decode('Ascii')

        data = list(data.split(","))

        if len(data) == 1:  # We will be receiving only Temperature through USB
            data = data[::-1]
            day = date.today()
            today = day.strftime("%d/%m/%Y")  # Conversion in day-month-year format
            data.append(today)
            noww = datetime.now()
            time = noww.strftime("%H:%M:%S.%f")  # Conversion in hour-min-sec-millisec format
            data.append(time)
            data = data[::-1]

            print(data)

            with open("2022-05-11.csv", "a", newline="") as xlsxfile:
                xlsxwriter = Xlsx.writer(xlsxfile)
                xlsxwriter.writerow(data)