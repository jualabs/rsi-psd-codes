import socket,socketloss

HOST = 'localhost'
PORT = 12000
s = socketloss.socketLoss(socket.AF_INET, socket.SOCK_DGRAM)
s.setLossProb(0.5)
s.settimeout(2.0)
s.connect((HOST, PORT))
s.sendWithLoss("teste")
try:
    data = s.recvWithLoss(1024)
    print(data)
except socket.timeout:
    print("Timeout")

s.close()
