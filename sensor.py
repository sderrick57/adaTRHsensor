#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
#hellokitty

# add ../../Sources to the PYTHONPATH
import time
#from apogee import *
import csv


if target == 'check':
        # retreive all sensor data
        print('TOP LEVEL');


        # Data pull from apogee.py
        #a1 = Quantum1()

        #print('%2.1f' % tempT.get_currentValue() + " deg F   " + "%2.1f" % humidT.get_currentValue() + "%  " + "%4.1f" % a1.get_micromoles() + " mmoles")

        print('BOTTOM LEVEL');

        #a2 = Quantum2()

        #print('%2.1f' % tempB.get_currentValue() + " deg F   " + "%2.1f" % humidB.get_currentValue() + "%  " + "%4.1f" % a2.get_micromoles() + " mmoles")

        print('TEST COMPLETE');

if target == 'log':
        # log all sensor data
        filename = str(raw_input('log file name: '))
        testlength = int(raw_input('Test Period (in min): '))
        testint = testlength * 60
        with open(filename + '.csv', 'wb') as csvfile:
                        sensorwriter = csv.writer(csvfile, delimiter= ' ', quotechar= '|', quoting=csv.QUOTE_MINIMAL)



                        # Data pull from apogee.py
                        #a1 = Quantum1()
                        #a2 = Quantum2()
                        #a1.__init__()
                        #a2.__init__()


                        sensorwriter.writerow(['UTC Time','Top Temperature','Top Humidity','Bottom Temperature','Bottom Humidity'])
                        while (testint > 0):
                                from time import gmtime, strftime
                                datalist = [strftime('%b %d %Y %H:%M:%S', gmtime())]
                                datalist.append('%2.1f' % )
                                datalist.append("%2.1f" % )
                                #datalist.append("%4.1f" % a1.get_micromoles())
                                datalist.append('%2.1f' % )
                                datalist.append("%2.1f" % )
                                #datalist.append('%4.1f' % a2.get_micromoles())
                                print(datalist)
                                sensorwriter.writerow(datalist)
                                testint = testint - 10
                                time.sleep(8)
