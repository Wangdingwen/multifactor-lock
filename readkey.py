#Python3
#Require rood permission
import sys
#import gpiolock
from evdev import InputDevice
from select import select

KEYBOARD_EVENT = "event0"
KEY_ENTER = 96
KEY_DEL = 1
KEY_0 = 82
KEY_1 = 79
KEY_2 = 80
KEY_3 = 81
KEY_4 = 75
KEY_5 = 76
KEY_6 = 77
KEY_7 = 71
KEY_8 = 72
KEY_9 = 73
key = {KEY_0: '0', KEY_1: '1', KEY_2: '2', KEY_3: '3', KEY_4: '4', KEY_5: '5', KEY_6: '6', KEY_7: '7', KEY_8: '8', KEY_9: '9'}

def detectInputKey(count, show):
    msg = ''
    empty = ' '
    counta = count
    if count == -1:
        flag = 0
    else:
        flag = 1
    dev = InputDevice('/dev/input/'+ KEYBOARD_EVENT)
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.value == 1 and event.code != 0:
                if event.code in key:
                    msg = msg + key[event.code]
                    counta = counta - flag
                    if show:
                        sys.stdout.write('\r')
                        sys.stdout.write(str(msg))
                        sys.stdout.flush()
                if event.code == KEY_DEL:
                    msg = msg[:-1]
                    counta = counta + flag
                    if show:
                        sys.stdout.write('\r')
                        sys.stdout.write(empty*count)
                        sys.stdout.write('\r')
                        sys.stdout.write(str(msg))
                        sys.stdout.flush()
                if (flag == 0 and event.code == KEY_ENTER) or (flag == 1 and counta == 0):
                    print('')
                    return msg

'''
def detectInputKey():
    dev = InputDevice('/dev/input/event0')
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.value == 1 and event.code != 0:
                print("Key: %s Status: %s" % (event.code, "pressed" if event.value else "release"))

detectInputKey()
'''
