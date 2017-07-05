import serial
import threading
ser = serial.Serial('/dev/ttyUSB2')

serR = ser.readline()

if serR.startswith('Temp: ') is True:
	logT = []
	logT.append(serR)

if serR.startswith('Hum: ') is True:
	logH = []
	logH.append(serR)

print(logT)
print(logH)
