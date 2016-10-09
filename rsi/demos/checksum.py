import random
import sys
import numpy.random as nprnd

TOT_PKTS = 100000
PKT_BYTES = 500
BER = 0.000001

def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = msg[i] + (msg[i+1] << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff

def genNoise(BER):
    n = 0
    for i in range(0,8):
        p = random.random()
        b = 0
        if p < BER:
           b = 1 << i
        n += b
    return n

def addNoise(BER,msg):
    n = 0
    newmsg = map(lambda v: v ^ genNoise(BER),msg)
#    for i in range(0,len(msg)):
#	noise = genNoise(BER)
#	newmsg.append(int(msg[i] ^ noise))
    return newmsg 

if __name__ == "__main__":
    if len(sys.argv) <= 3:
	print("Usage: checksum.py <total-pkts> <pkt-size> <BER>")
	sys.exit(2)
    serverIp = sys.argv[1]
    serverPort = int(sys.argv[2])
    user = sys.argv[3]
    TOT_PKTS = int(sys.argv[1])
    PKT_BYTES = int(sys.argv[2])
    BER = float(sys.argv[3])
    npkts = 0
    npkts_error = 0.0
    npkts_chks = 0.0
    while npkts < TOT_PKTS:
	#mbytes = [random.randint(0,255) for i in xrange(PKT_BYTES)]
	mbytes = nprnd.randint(255, size=PKT_BYTES).tolist()
        npkts += 1
	pad = len(mbytes)%2
	mbytes.extend([0]*pad)
	c1=checksum(mbytes)
        mbytes_noise = addNoise(BER,mbytes) #passar por um canal com erro
        c2=checksum(mbytes_noise)
        if (cmp(mbytes,mbytes_noise) != 0):
           npkts_error += 1
	if (c1 != c2):
           npkts_chks += 1
    print("Total de pkts: %d"%npkts)
    print("Pkts com erro: %d"%npkts_error)
    print("Pkts detectados pelo checksum: %d"%npkts_chks)
    if npkts_error>0:
	print("Eficiencia do checksum: %f"%(npkts_chks/npkts_error))
