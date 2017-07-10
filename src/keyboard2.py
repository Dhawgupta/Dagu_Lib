#!/usr/bin/env python
# https://learn.pimoroni.com/tutorial/robots/controlling-your-robot-wireless-keyboard

import usb.core
import usb.util
import serial
import time

ard = serial.Serial('/dev/ttyACM0',19200)


USB_VENDOR  = 0x3938 # Rii
USB_PRODUCT = 0x1032 # Mini Wireless Keyboard

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

BTN_LEFT  = 80
BTN_RIGHT = 79
BTN_DOWN  = 81
BTN_UP    = 82
BTN_STOP  = 44 # Space
BTN_EXIT  = 41 # ESC

dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)
endpoint = dev[0][(0,0)][0]
if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)



while True:
    control = None
    try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
    except:
        pass

    if control != None:
        if BTN_DOWN in control:
            ard.write('szz')
    #      print "Going back"

        if BTN_UP in control:
            ard.write('wzz')
            print "Going Forward"

        if BTN_LEFT in control:
            ard.write('aZz')


        if BTN_RIGHT in control:
	        ard.write('dzZ')


        if BTN_STOP in control:
            ard.write('xaa')

    #    print "Stopped"

        if BTN_EXIT in control:
            exit()
