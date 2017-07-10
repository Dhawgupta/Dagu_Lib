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
        self.lastThrottle = 0
    #entering the analog value for left adn right wheel between 0 - 100
    def map(self, val,inputL, inputH, outputL , outputH ):
        val1 = (float(val)/(inputH - inputL))*(outputH - outputL ) + outputL
        return int(val1)
    def forward(self,aleft, aright):
        aleft = self.map(aleft, 0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.car.write('w' + chr(aleft) + chr(aright))

    def right(self,aleft, aright):
        aleft = self.map(aleft,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.car.write('d' + chr(aleft) + chr(aright))

    def left(self,aleft, aright):
        aleft = self.map(aleft,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.car.write('a' + chr(aleft) + chr(aright))

    def reverse(self,aleft, aright):
        aleft = self.map(aleft,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.car.write('s' + chr(aleft) + chr(aright))

    def stop(self,aleft = 0, aright = 0):
        aleft = self.map(aleft,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        aright = self.map(aright,0, 100, self.Lval_for_motor, self.Hval_for_motor )
        self.car.write('x' + chr(aleft) + chr(aright))

    def throttle(self, throt):
        self.forward(throt, throt)
        self.lastThrottle
    def brake(self, mode = 0 , brak = 100):
        # crearing different kind of modes
        '''
        mode = 0 => taking the forward pwm to 0
        mode = 1 => enabling the halt feature in motor driver"
        mode = 2 => delayed halt while taking pwm down slowly
        '''
        if mode == 0:
            self.forward(0,0)
        elif mode == 1:
            self.stop()
        elif mode == 2:
            while self.lastThrottle > 0:
                self.forward(self.lastThrottle, self.lastThrottle)
                self.lastThrottle = self.lastThrottle - brak
                # tune the sleep value
                time.sleep(0.01)
