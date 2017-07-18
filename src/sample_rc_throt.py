#!/usr/bin/env python

import time
import serial
class car:
    def __init__(self, port = '/dev/ttyACM0',baud_rate = 9600):
        try:
            self.car = serial.Serial(port, 9600)
            print "Arduino connected on port {}".format(port)
	    print "Waiting for it to boot"
            time.sleep(5)
        except (RuntimeError, TypeError, NameError):
            print "Not able to connect arduino on port {}".format(port)
	    exit()
	
        self.Lval_for_motor = 0; # this is the lower value of PWM for motor
        self.Hval_for_motor = 255;
        self.alef = 0 # are from 0 -255
        self.arig = 0 # from 0 -255

        self.lastThrottle = 0

    def map(self, val,inputL, inputH, outputL , outputH ):  # converts from 0 -100 to  0 -255
        if val > inputH:
            val = inputH
        if val < inputL:
            val = inputL
        val1 = (float(val)/(inputH - inputL))*(outputH - outputL ) + outputL

        return int(val1)
    def forward(self, aleft,aright):
        # self.speedl = aleft
        # self.speedr = aright
        # aleft = self.map(aleft, 0, 100, self.Lval_for_motor, self.Hval_for_motor )
        # aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.alef = aleft
        self.arig = aright
        self.car.write('w' + chr(self.alef) + chr(self.arig))

    def stop(self):
        aleft = 0
        aright = 0
        # self.speedl = aleft
        # self.speedr = aright
        self.alef = aleft
        self.arig = aright
        self.car.write('x' + chr(self.alef) + chr(self.arig))

    def throttle(self, throt): # positive for accelration and -ve for breaking
        # throttle value will be between 0 - 100
        # we will run a loop which will change the speed of vheel basically rate in chaneg of voltage
        if(throt > 0):
	    print "Alef = {}, Arig = {}".format(self.alef, self.arig)
            if(self.alef >= 220 or self.arig >= 220):
                print "Max Speed Achieved"
		return False
            else:
                self.forward(self.alef +  throt , self.arig + throt)
                time.sleep(0.01)# add a custom time if required
		return True
        if(throt < 0):
            if(self.alef <= 20 or self.arig   <= 20):
                print "Min Speed Achieved"
		return False
            else:
                self.forward(self.alef +  throt , self.arig + throt)
                time.sleep(0.01)# add a explicit dt if required by using this timer
		return True
