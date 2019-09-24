import socket
from threading import Thread
import sys
#클라이언트 소켓
def smsg(sckt):
    while True:
        sckt.send(input().encode())

def rmsg(sckt):
    while True:
        sys.stdout.flush()
        print(sckt.recv(4096).decode())

csocket = socket.socket()
csocket.connect(('127.0.0.1',12345))

st = Thread(target = smsg, args = [csocket])
rt = Thread(target = rmsg, args = [csocket])
st.start()
rt.start()