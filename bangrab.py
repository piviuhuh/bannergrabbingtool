import socket 

ipadd = input("Insert IP Address")
nport = input("Insert port)

nport = int(nport)

mysckt = socket.socket()

mysckt.connect((ipadd,nport))

answ = mysckt.recv(1024)
print(answ)
