#Python 3
import os, time
import bluetooth, threading, socket

def receive(bt_addr):
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((bt_addr, 1))
    while True:
        #time.sleep(2)
        data = client_socket.recv(1).decode('utf-8')
        if data != None:
            for i in range(1,32):
                data = data + client_socket.recv(1).decode('utf-8')
            return data


def auth(id,data):
    os.system('echo ' + data + '>nfc/nfc-temp.txt')
    if os.system('diff nfc/nfc-temp.txt nfc/' + str(id) + '.txt') == 0:
        return 0
    else:
        return -2

def receive_auth_all(bt_addr):
    data = receive(bt_addr)
    if data == -1:
        return -1
    for i in range(1,len([name for name in os.listdir('nfc/') if os.path.isfile(os.path.join('nfc/', name))])):
        if auth(i,data) == 0:
            return i
    return -2

#print(receive_auth_all('98:D3:21:FC:81:0F'))
