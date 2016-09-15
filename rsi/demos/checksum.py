def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff

if __name__ == "__main__":
    f = open("alienista.txt","r")
    for m in f:
	pad = len(m)%2
	c=checksum(m+" "*pad)
	print(m, c)
	#passar por um canal com erro
	#computar checksum
	#comparar checksum
    f.close()
