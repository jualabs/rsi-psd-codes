# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:25:03 2018

@author: Glauco
"""
import random
import os 
import time
from struct import unpack
from functools import reduce

def complementarySum(word1,word2):
    result = word1 + word2
    if result >= 65536:
        result = (result & 0xFFFF) + 0x1
    return result

def checksum(data):
    stringUnpack = 'H'*int(len(data)/2)
    stringUnpack = '>' + stringUnpack
    words = unpack(stringUnpack,data)
    result = reduce(complementarySum, words)
    return result.to_bytes(2,byteorder="big")

def transfer(pkt, BER):
    bitError = random.choices([0,1],[1-BER,BER],k=len(pkt)*8)
    stringError = str(bitError)[1:-1].replace(", ","")
    intError = int(stringError,2)
    pktWithError = int.from_bytes(pkt,byteorder="big") ^ intError
    newPkt = pktWithError.to_bytes(len(pkt),byteorder="big")
    if intError > 0:
        error = True
    else:
        error = False
    return (newPkt,error)

if __name__ == "__main__":
    """ define parameters """
    BER = 10**-4
    nPkts = 1000
    pktSize = 500
    """ define metrics """
    no_changes = 0.0
    changed = 0.0
    changed_error_detected = 0.0
    changed_non_detected = 0.0    
    
    """ simulation """
    for p in range(nPkts):
        """ generate data """
        data = os.urandom(pktSize)
        """ padding data """
        if len(data) % 2 == 1:
            data += b'\x00'
        """ compute checksum """
        chk = checksum(data)
        """ create packet """
        pkt = data + chk
        """ transfer data """        
        (pkt_,error) = transfer(pkt, BER)
        """ split trasmitted packet and checksum """
        data_ = pkt_[0:-2]
        chk_= pkt_[len(data):]
        """ compute checksum from the transmitted packet """
        chk__ = checksum(data_)
        """ check if data is ok """
        if error:
            changed += 1
            if chk__ == chk_:
                """ Packet with error, but undetected """
                changed_non_detected += 1
            else:
                """ Packet with error and undetected """
                changed_error_detected += 1
        else:
            no_changes += 1
            if chk__ != chk_:
                print("Houston we have a problem!")
            
    print("Packets with error:",100*changed/(no_changes+changed),"%")
    if changed > 0:
        print("Packets with error detected by checksum:",100*changed_error_detected/changed,"%")
        print("Packets with undetected errors:",100*changed_non_detected/changed,"%")