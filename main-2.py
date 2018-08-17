#Python3
import os, time
import arduino_nfc, blueclient
import gpiolock

#gpiolock.lock()
while True:
    os.system('rm status/*')
    try:
        blue = blueclient.receive("98:D3:61:FD:51:29")
        if  blue == 'SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4':
            print('BLUETOOTH OK')
            os.system('touch status/bluetooth.txt')
            nfcr = arduino_nfc.receive_auth_all('98:D3:21:FC:81:0F')
            if nfcr >= 0:
                print('NFC OK')
                print('ALL OK')
                #gpiolock.unlock()
            else:
                print(False)
                break
    except:
        continue
