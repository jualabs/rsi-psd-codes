import sys
import random
from socket import *

cnt =0

def connection(ip,port):
  global cnt
  cnt = 0
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((ip,port))
  return clientSocket

def hardClose(sckt):
  sckt.close()  

def softClose(sckt):
  global cnt
  sckt.send(cnt+" TERM")
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.split(" ")
  if (mess[1] == "OK"):
    sckt.close()
  else:
    print("Alguma coisa deu errada!")
    sckt.close()

#test acknowledgment phase
#bad = 1 iff the user does not exist
#bad = 0 iff the user exists
def test1(sckt, user, bad):
  global cnt
  sckt.send(cnt+" CUMP "+user)
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.split(" ")
  if (mess[0] == cnt-1):
    return -2
  if (mess[1] == "OK"):
    return -1 if bad == 1 else 1
  elif (mess[1] == "NOK"):
    return 1 if bad == 1 else -1
  else 
    return -2

#test not expected commands
def test2(sckt):
  global cnt
  sckt.send("TRAP")
  cnt += 1
  data, addr = sckt.recvfrom(2048)
  mess = data.split(" ")
  if (mess[0] == cnt-1):
    return -2
  if (mess[1] == "NOK"):
    return 1
  else:
    return -1

#test list phase
def test3(sckt):
  global cnt
  sckt.send(cnt+" LIST")
  cnt += 1
  data1 = ""
  while 1:
    data, addr = sckt.recvfrom(2048)
    data1 += data
    if ":END:" in data:    
	break
  
  mess = data1.split(" ")
  if (mess[0] == cnt-1):
    return (-2,"")
  if (mess[1] == "ARQS"):
    return (1,mess[2])
  elif (mess == "NOK"):
    return (0,"")
  else 
    return (-2,"")

if __name__ == "__main__":
  if len(sys.argv) <= 4:
    print("Usage: pta-client.py <server-ip> <server-port> <user>")
  serverIp = sys.argv[1]
  serverPort = int(sys.argv[2])
  user = sys.argv[3]

  #Testing bad CUMP command
  cSocket = connection(serverIp,serverPort)
  points += test1(cSocket,"laser1212",1)
  hardClose(cSocket)

  #Testing bad command
  cSocket = connection(serverIp,serverPort)
  points += test2(cSocket)
  hardClose(cSocket)

  #Testing good CUMP command
  cSocket = connection(serverIp,serverPort)
  points += test1(cSocket,user,0)
  
  #Testing LIST
  (points,arqs) += test3(cSocket)
  arq = random.choice(arqs.split(","))
  
  #Testing ARQ
  if arq:
     points += test4(cSocket) 
  else:
     
