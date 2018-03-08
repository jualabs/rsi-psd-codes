# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:32:04 2018

@author: Glauco
"""

import subnetcalc as sb

"""
    Each entry in this table indicates the network address, 
    the network mask, and the forwarding interface.
"""
table = {
            ('41.0.1.0','24'): 3,
            ('41.0.1.192','26'): 2,
            ('20.100.0.0','19'): 1,
            ('0.0.0.0','0'): 4
        }

"""
    Each entry in the list below is the destination address
    of a given packet.
"""
packets = ['20.100.32.1','41.0.1.200']

def routing(ip):
    """
        Receives the destination ip address and chooses the route
        based on the longest prefix match.
        
        Returns the forwarding interface
    """
    bestroute = None
    for route in table.keys():    
        (net, broad) = sb.getNetAndBroadAddr(route[0],route[1])
        dest = sb.ip2int(ip)
        if (net <= dest) and (dest <= broad):
            if not bestroute:
                bestroute = route
            elif int(route[1]) > int(bestroute[1]):
                bestroute = route
    return table[bestroute]

for ip in packets:
    intf = routing(ip);
    print("The packet with dest addr",ip,"will be forwarded to interface", intf)