#Python3
import os, time
import arduino_nfc, blueclient
import gpiolock

gpiolock.lock()
while True:
    time.sleep(2)
    #gpiolock.lock()
    try:
        blue = blueclient.receive("98:D3:61:FD:51:29")
        if  blue == 'SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4':
            print('BLUETOOTH OK')
            os.system('touch status/bluetooth.txt')
            try:
                start=time.perf_counter()
                nfcr = arduino_nfc.receive_auth_all('98:D3:21:FC:81:0F')
                if time.perf_counter()-start >=30:
                    print(False)
                    gpiolock.auto_lock()
                    continue
                if nfcr >= 0:
                    print('NFC OK')
                    print('ALL OK')
                    os.system('rm status/bluetooth.txt')
                    gpiolock.auto_unlock()
                else:
                    print(False)
                    gpiolock.auto_lock()
                    continue
            except:
                continue
    except:
        continue
