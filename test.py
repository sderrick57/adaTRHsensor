import serial
ser = serial.Serial('/dev/ttyUSB2')

serR = ser.readline()

serlog = 0

while True:

	if serR.startswith('Temp: ') is True:
		logT = []
		serR = serR[-7:-2]
		logT.append(serR)

	if serR.startswith('Hum: ') is True:
		logH = []
		serR = serR[-7:-2]
		logH.append(serR)

	serR = ser.readline()

	serlog = serlog + 1

	if serlog > 200:
			break

print(logT)
print(logH)
