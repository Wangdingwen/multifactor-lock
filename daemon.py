#Python3
#Require rood permission
import os, time
import arduino_nfc, totpauth, passwd
import gpiolock
from evdev import InputDevice
from select import select

KEYBOARD_EVENT = "event0"
KEY_ENTER = 11
KEY_0 = 0
KEY_1 = 1
KEY_2 = 2
KEY_3 = 3
KEY_4 = 4
KEY_5 = 5
KEY_6 = 6
KEY_7 = 7
KEY_8 = 8
KEY_9 = 9
key = {KEY_0: '0', KEY_1: '1', KEY_2: '2', KEY_3: '3', KEY_4: '4', KEY_5: '5', KEY_6: '6', KEY_7: '7', KEY_8: '8', KEY_9: '9'}


def detectInputKey(count):
    msg = ''
    if count == -1:
        flag = 0
    else:
        flag = 1
    dev = InputDevice('/dev/input/'+ KEYBOARD_EVENT)
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.value == 1 and event.code != 0:
                if (flag == 0 and event.code == KEY_ENTER) or (flag == 1 and count == 0):
                    return msg
                elif event.code in key:
                    msg = msg + key[event.code]
                    count = count - flag
                #print("Key: %s Status: %s" % (event.code, "pressed" if event.value else "release"))

def open():
    if os.path.exists('status/bluetooth.txt'):
        gpiolock.unlock()
    else:
        if arduino_nfc.receive_auth_all('98:D3:21:FC:81:0F') >= 0:
            gpiolock.unlock()
    

while True:
    detectInputKey(-1)
    ikey = detectInputKey(1)
    if ikey == 1:
        if totpauth.auth_all(detectInputKey(6)):
            open()
