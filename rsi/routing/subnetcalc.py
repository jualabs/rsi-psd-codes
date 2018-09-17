# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:42:51 2018
@author: Glauco
"""

def ip2int(ip):
    """
        Helper function that converts ip from string
        to integer for better manipulation.
    """
    addr = 0
    pos = 24
    for i in ip.split("."):
        addr += int(i) << pos
        pos -= 8
    return addr

def int2ip(addr):
    """
        Helper function that converts ip from integer
        to string for better presentation.
    """
    ip = ""
    pos = 24
    for i in range(4):
        byte = 255 << pos
        ip += str((addr & byte) >> pos)
        if pos > 0:
            ip += "."
        pos -= 8
    return ip   

def getNetAndBroadAddr(netaddr, netmask):
    """
        Helper function that receives an IP address
        and a netmask and calculates the 
        respective network and broadcast addresses.
        
        The input data is assumed to be string, and 
        the returned addresses are integers for better 
        manipulation.
    """
    addr = ip2int(netaddr)
    mask = (2 ** 32 -1) - (2 ** (32-int(netmask)) -1)
    net = (addr & mask)
    broad = (net | (2 ** (32-int(netmask)) -1))
    return (net,broad)
    
if __name__ == "__main__":
    netaddr = "192.168.1.242"
    netmask = "24"
    net,broad = getNetAndBroadAddr(netaddr,netmask)
    print("Network Address",int2ip(net))
    print("First Host Address",int2ip(net+1))
    print("Last Host Address",int2ip(broad-1))
    print("Broadcast Address",int2ip(broad))