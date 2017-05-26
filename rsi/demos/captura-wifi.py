import pcap, dpkt, binascii

maxPkts = 10
nPkts=0

for ts, pkt in pcap.pcap(name='wlan1'):
	try:
		rtap = dpkt.radiotap.Radiotap(pkt)
	except:
		pass
	wifi = rtap.data
	if wifi.type == 0 and wifi.subtype == 4:
		print("Mostrando o pacote #"+str(nPkts))
		src = binascii.hexlify(wifi.mgmt.src)
		ssid = wifi.ies[0].info
		print(ts, src, ssid)
		nPkts += 1
		print("\n")

	if (nPkts == maxPkts):
		break
