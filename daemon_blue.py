#!/usr/bin/python3
import time
import bluetooth, threading, socket
import totpauth
import gpiolock
import RPi.GPIO as GPIO

def receive(bt_addr):
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        client_socket.connect((bt_addr, 1))
        while True:
            #time.sleep(2)
            data = client_socket.recv(1).decode('utf-8')
            if data != None:
                for i in range(1,6):
                    data = data + client_socket.recv(1).decode('utf-8')
                return data
    except:
        return 1

#print(receive("E4:58:B8:50:88:FE"))
GPIO.setup(36,GPIO.OUT)
while True:
    if not GPIO.input(36):
        continue
    data = receive("E4:58:B8:50:88:FE")
    if data != 1:
        if totpauth.auth_all(data) >= 0:
            gpiolock.auto_unlock()
        else:
            gpiolock.auto_lock()