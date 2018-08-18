import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

def lock():
    GPIO.output(37,False)

def unlock():
    GPIO.output(37,True)

def light_green(sett):
    GPIO.output(38,not sett)

def light_red(sett):
    GPIO.output(40,not sett)

def auto_unlock():
    unlock()
    light_green(True)
    time.sleep(5)
    lock()
    light_green(False)

def auto_lock():
    lock()
    light_red(True)
    time.sleep(3)
    light_red(False)
