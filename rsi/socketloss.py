import socket, random, time

class socketLoss(socket.socket):
    lossProb = 0.0

    def setLossProb(self, p):
        self.lossProb = float(p)

    def getLossProb(self):
        return self.errorProb
    
    def sendWithLoss(self, s):
        if (self.type == socket.SOCK_DGRAM):
            u = random.random()
            if (u>self.lossProb):
                self.send(s)
        else:
            self.send(s)

    def recvWithLoss(self, n):
        if (self.type == socket.SOCK_DGRAM):
            data = self.recv(n)
            u = random.random()
            if (u>self.lossProb):
                return data
            else:
                raise socket.timeout
        else:
            return self.recv(n)        
