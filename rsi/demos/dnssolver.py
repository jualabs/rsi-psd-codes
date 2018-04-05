# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:06:42 2018

@author: Glauco
"""

import dns.name
import dns.message
import dns.query
import dns.flags
import random

def consulta(nome, servidor, tipo):
    nome = nome
    servidor_dns = servidor
    ADDITIONAL_RDCLASS = 65535

    nome = dns.name.from_text(nome)
    if not nome.is_absolute():
        nome = nome.concatenate(dns.name.root)

    requisicao = dns.message.make_query(nome, tipo)
    requisicao.flags |= dns.flags.AD
    requisicao.find_rrset(requisicao.additional, dns.name.root, ADDITIONAL_RDCLASS,
                       dns.rdatatype.OPT, create=True, force_unique=True)
    resposta = dns.query.udp(requisicao, servidor_dns)
    return resposta

def trata_resposta(resposta_dns, tipo):
    splitted_reg = map(lambda x: x.to_text().split(" "), resposta_dns)
    A_reg = filter(lambda x: x[3] == tipo, splitted_reg)
    name_ip_regs = map(lambda x: (x[0],x[4]), A_reg)
    return list(name_ip_regs)

def recursiva(nome, servidor_raiz, tipo):
    print("Consultando servidor raiz", servidor_raiz, "para o nome", nome)
    resposta = consulta(nome,servidor_raiz,tipo)
    while (resposta.answer == []):
        #No authoritative response
        if (resposta.additional == []):
            NS_reg = resposta.authority[0][0]
            print("Encontrando IP de servidor DNS", NS_reg)
            nome_ip_regs = recursiva(str(NS_reg), servidor_raiz, dns.rdatatype.A)
            servidor_dns = nome_ip_regs[0]
            print("Encontrado IP",servidor_dns[1],"para servidor DNS",servidor_dns[0])
        else:
            #Choosing a random server to query
            nome_ip_regs = trata_resposta(resposta.additional,"A")
            servidor_dns = random.sample(nome_ip_regs,1)[0]
            
        print("Não encontrado! Consultando servidor DNS", servidor_dns[0])        
        resposta = consulta(nome,servidor_dns[1],tipo)
    
    nome_ip_regs = trata_resposta(resposta.answer,"A")
    return nome_ip_regs
    
nome = 'www.ufrpe.br'
servidor_raiz = '192.36.148.17'

nome_ip_regs = recursiva(nome, servidor_raiz, dns.rdatatype.A)
for reg in nome_ip_regs:
    print("Encontrado! IP de",reg[0],"é",reg[1])