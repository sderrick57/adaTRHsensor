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

	if serlog > 100:
			break

logT = map(int, logT)
logH = map(int, logH)

avgT = sum(logT) / len(logT)
avgH = sum(logH) / len(logH)
print(logT)
print(avgT)
print(logH)
print(avgH)
