import serial
ser = serial.Serial('/dev/ttyUSB1')



serlog = 0
logT = []
logH = []


while serlog < 100:
	serR = ser.readline()
	if serR.startswith('Temp: ') is True:

		serR = serR[6:-2]
		logT.append(serR)

	if serR.startswith('Hum: ') is True:

		serR = serR[5:-2]
		logH.append(serR)

	else:
		break

	serlog = serlog + 1

logT = map(float, logT)
logH = map(float, logH)

avgT = sum(logT) / len(logT)
avgH = sum(logH) / len(logH)

print(avgT)
print(avgH)
