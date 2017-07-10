#!/usr/bin/env python

import time
import serial
class car:
    def __init__(self, port = '/dev/ttyACM0',baud_rate = 9600):
        try:
            self.car = serial.Serial(port, 9600)
            print "Arduino connected on port {}".format(port)
        except (RuntimeError, TypeError, NameError):
            print "Not able to connect arduino on port {}".format(port)
        self.Lval_for_motor = 0; # this is the lower value of PWM for motor
        self.Hval_for_motor = 255;
        self.alef = 0
        self.arig = 0
        self.lastThrottle = 0

    def map(self, val,inputL, inputH, outputL , outputH ):
        if val > inputH:
            val = inputH
        if val < inputL:
            val = inputL
        val1 = (float(val)/(inputH - inputL))*(outputH - outputL ) + outputL

        return int(val1)
    def forward(self, aleft,aright):
        aleft = self.map(aleft, 0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.alef = aleft
        self.arig = aright
        self.car.write('w' + chr(aleft) + chr(aright))

    def stop(self):
        aleft = 0
        aright = 0
        self.alef = aleft
        self.arig = aright
        self.car.write('x' + chr(aleft) + chr(aright))

    def throttle(self, throt): # positive for accelration and -ve for breaking
        # throttle value will be between 0 - 100
        # we will run a loop which will change the speed of vheel basically rate in chaneg of voltage
        if(throt > 0):
            if(self.alef == 100 || self.arig == 100):
                print "Max Speed Achieved"
            else:
                forward(self.alef +  throt , self.arig + thort)
                time.sleep(0.01)
        if(throt < 0):
            if(self.alef == 0 || self.arig == 0):
                print "Min Speed Achieved"
            else:
                forward(self.alef -  throt , self.arig - thort)
                time.sleep(0.01)
