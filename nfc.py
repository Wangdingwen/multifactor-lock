#Python 3
import os

def read():
    return os.system('nfc-poll>nfc/nfc-temp.txt')

def auth(id):
    if os.system('diff nfc/nfc-temp.txt nfc/' + str(id) + '.txt') == 0:
        return 0
    else:
        return -2

def read_auth_all():
    if read() == 0:
        for i in range(1,len([name for name in os.listdir('nfc/') if os.path.isfile(os.path.join('nfc/', name))])):
            if auth(i) == 0:
                return i
        return -2
    else:
        return -1

print(read_auth_all())