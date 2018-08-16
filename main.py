import os, time
import nfc, blueclient, totpauth, passwd
import gpiolock

gpiolock.lock()
while True:
    blue = blueclient.receive("98:D3:61:FD:51:29")
    if  blue == 'SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4':
        nfcr = nfc.read_auth_all()
        if nfcr >= 0:
            if totpauth.auth(nfcr,input()):
                gpiolock.unlock()
            else:
                print(False)
                break
        else:
            print(False)
            break
    elif blue != 1:
        print(False)
        break