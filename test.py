import serial
import threading
ser = serial.Serial('/dev/ttyUSB2')

serR = ser.readline()

if serR.startswith('Temp: ') is True:
	log = []
	log.append(serR)
