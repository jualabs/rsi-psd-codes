import socket, random

class socketError(socket.socket):
    errorProb = 0.0

    def setErrorProb(self, p):
        self.errorProb = float(p)

    def getErrorProb(self):
        return self.errorProb
    
    def sendWithError(self, s):
        if (self.type == socket.SOCK_DGRAM):
            u = random.random()
            if (u>self.errorProb):
                self.send(s)
        else:
            self.send(s)

    def recvWithError(self, n):
        if (self.type == socket.SOCK_DGRAM):
            u = random.random()
            if (u>self.errorProb):
                return self.recv(n)
            else:
                return b"Error"
        else:
            return self.recv(n)        

HOST = 'localhost'
PORT = 12000
s = socketError(socket.AF_INET, socket.SOCK_DGRAM)
s.setErrorProb(0.5)
s.connect((HOST, PORT))
s.sendWithError("teste")
data = s.recvWithError(1024)
print(data)
s.sendWithError("testando")
data = s.recvWithError(1024)
print(data)
s.close()
