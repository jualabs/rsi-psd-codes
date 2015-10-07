import socket,socketerror

HOST = 'localhost'
PORT = 12000
s = socketerror.socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.5)
s.settimeout(2.0)
s.connect((HOST, PORT))
s.sendWithError("teste")
try:
    data = s.recvWithError(1024)
    print(data)
except socket.timeout:
    print("Timeout")

s.sendWithError("testando")

try:
    data = s.recvWithError(1024)
    print(data)
except socket.timeout:
    print("Timeout")

s.close()
