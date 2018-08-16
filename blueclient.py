import time
import bluetooth, threading, socket

def receive(bt_addr):
    client_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        client_socket.connect((bt_addr, 1))
        client_socket.send("R")
        time.sleep(1)
        data = client_socket.recv(1024).decode('utf-8')
        return data
    except:
        return 1

print(receive("98:D3:61:FD:51:29"))