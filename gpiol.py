import RPi.GPIO as GPIO
import time, os
from nfc import read_auth

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

GPIO.output(37,True)
GPIO.output(35,True)
GPIO.output(33,True)
GPIO.output(31,True)

while True:
    r = read_auth()
    if r == 0:
        GPIO.output(35,True)
        GPIO.output(31,False)
    elif r == 1:
        GPIO.output(35,True)
        GPIO.output(31,True)
    else:
        GPIO.output(35,False)
        GPIO.output(31,True)
    time.sleep(2)
    GPIO.output(35,True)
    GPIO.output(33,True)
    GPIO.output(31,True)

GPIO.cleanup()