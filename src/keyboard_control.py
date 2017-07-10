#!/usr/bin/env python

from car_lib import *
import usb.core
import usb.util
import serial
import time

dagu = car('/dev/ttyACM0', 19200)


USB_VENDOR  = 0x046d # Rii
USB_PRODUCT = 0xc31c # Mini Wireless Keyboard

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
            dagu.brake()
            print "Going back"

        if BTN_UP in control:
            dagu.throttle(75)
            print "Going Forward"

        if BTN_LEFT in control:
            dagu.left(40, 90)


        if BTN_RIGHT in control:
            dagu.right(90, 40)
            print "Going Right"

        if BTN_STOP in control:
            dagu.stop()
            print "Stopped"

        if BTN_EXIT in control:
            exit()
