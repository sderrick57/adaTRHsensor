import serial
import threading
ser = serial.Serial('/dev/ttyUSB0')
global serlog
serlog = []
def serthread(cx):
		global serlog
		while True:
    			if len(serlog) > 1000:
            			serlog.pop(-1)
        		try:
            			s = cx.readline()
            			serlog.insert(0,s)
        		except:
            			break
		print("comms closed")

t = threading.Thread(target=serthread, args=(ser,))
t.start()
