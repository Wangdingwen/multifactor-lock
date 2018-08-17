import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

def unlock():
    GPIO.output(37,False)

def lock():
    GPIO.output(37,True)
