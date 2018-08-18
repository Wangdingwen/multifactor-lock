#Python3
import time
import arduino_nfc, blueclient, totpauth, passwd
import gpiolock

gpiolock.lock()
while True:
    gpiolock.lock()
    time.sleep(2)
    try:
        blue = blueclient.receive("98:D3:61:FD:51:29")
        if  blue == 'SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4':
            print('BLUETOOTH OK')
            nfcr = arduino_nfc.receive_auth_all('98:D3:21:FC:81:0F')
            if nfcr >= 0:
                print('NFC OK')
                if totpauth.auth(nfcr,input()):
                    print('TOTP OK')
                    print('ALL OK')
                    gpiolock.auto_unlock()
                else:
                    print(False)
                    gpiolock.auto_lock()
                    continue
            else:
                print(False)
                gpiolock.auto_lock()
                continue
    except:
        continue
