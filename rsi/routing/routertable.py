# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:32:04 2018

@author: Glauco
"""

import subnetcalc as sb
import sys

"""
    Each entry in the list below is the destination address
    of a given packet.
"""
packets = ['20.100.32.1','41.0.1.200']

def forwarding(ip,tbl):
    """
        Receives the destination ip address and chooses the route
        based on the longest prefix match againt the routing table.
        Inputs:
            ip: ip address (string)
            tbl: routing table (dict whose the value is the forwarding interface and the key is a tuple with network address and netmask), each entry in this table indicates the network address, the network mask, and the forwarding interface.
        
        Returns: the forwarding interface
    """

    """
        Please change here
    """
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 3:
        tblfile = sys.argv[1]
        ip = sys.argv[2]
        try:
            tbl = dict()
            tblpointer = open(tblfile)
            for line in tblpointer:
                fields = line.split(",")
                tbl[(fields[0],fields[1])] = fields[2].strip("\n")
        except:
            print("Problem")
        intf = forwarding(ip,tbl);
        print("The packet with dest addr",ip,"will be forwarded to interface", intf)
    else:
        tblfile = "table"
        try:
            table = dict()
            tblpointer = open(tblfile)
            for line in tblpointer:
                fields = line.split(",")
                table[(fields[0],fields[1])] = fields[2].strip("\n")
        except:
            print("Problem")
        for ip in packets:
            intf = forwarding(ip,table);
            print("The packet with dest addr",ip,"will be forwarded to interface", intf)
