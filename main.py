import os, time
import arduino_nfc, blueclient, totpauth, passwd
import gpiolock

#gpiolock.lock()
while True:
    try:
        blue = blueclient.receive("98:D3:61:FD:51:29")
        if  blue == 'SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4':
            time.sleep(2)
            print('BLUETOOTH OK')
            nfcr = arduino_nfc.receive_auth_all('98:D3:21:FC:81:0F')
            if nfcr >= 0:
                print('NFC OK')
                if totpauth.auth(nfcr,input()):
                    print('ALL OK')
                    #gpiolock.unlock()
                else:
                    print(False)
                    break
            else:
                print(False)
                break
    except:
        continue