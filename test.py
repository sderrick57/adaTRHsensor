import serial
import threading
ser = serial.Serial('/dev/ttyUSB2')

serR = ser.readline()

serlog = 0

while True:
	if serR.startswith('Temp: ') is True:
		logT = []
		serR = serR[-5:-4]
		logT.append(serR)

	serR = ser.readline()

	if serR.startswith('Hum: ') is True:
		logH = []
		serR = serR[-4:-4]
		logH.append(serR)

	serR = ser.readline()

	serlog = serlog + 1

	if serlog > 201:
			break

print(logT)
print(logH)
