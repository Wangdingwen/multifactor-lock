import RPi.GPIO as GPIO
import time, os



GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

'''
while True:
    GPIO.output(37,True)
    time.sleep(2)
    GPIO.output(37,False)
    time.sleep(2)
'''

def unlock():
    GPIO.output(37,False)

def lock():
    GPIO.output(37,True)