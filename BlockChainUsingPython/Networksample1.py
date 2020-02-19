import socket
from threading import Thread
import sys
#서버소켓
def smsg(sckt):
    while True:
        sckt.send(input().encode())

def rmsg(sckt):
    while True:
        sys.stdout.flush()
        print(sckt.recv(4096).decode())

conSocket = socket.socket()
conSocket.bind(('127.0.0.1', 12345))
conSocket.listen(1)
sock, addr = conSocket.accept()

st = Thread(target = smsg, args = [sock])
rt = Thread(target = rmsg, args = [sock])
st.start()
rt.start()