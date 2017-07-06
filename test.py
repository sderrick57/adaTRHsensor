import serial
ser = serial.Serial('/dev/ttyUSB1')

serR = ser.readline()

serlog = 0

while serlog < 100:

	if serR.startswith('Temp: ') is True:
		logT = []
		serR = serR[6:-2]
		logT.append(serR)

	if serR.startswith('Hum: ') is True:
		logH = []
		serR = serR[5:-2]
		logH.append(serR)

	serR = ser.readline()

	serlog = serlog + 1

logT = map(float, logT)
logH = map(float, logH)

avgT = sum(logT) / len(logT)
avgH = sum(logH) / len(logH)
print(logT)
print(avgT)
print(logH)
print(avgH)
