import csv
from socket import *
import time
from remove_vlan_bridge import remove_vlan
from adiciona_vlan_bridge import adiciona_vlan


print ('Sistema de alteração de VLAN em massa via Planilha .CSV\n\n')

## ip do anm/unm, user e senha TL1, vlan e ip da olt
server = input ("Informe o IP do Servidor: ")
user = input ("Informe o login administrador: ")
password = input ("Informe a senha do administrador: ")
vlan = input ("Informe a VLAN a ser adicionada à ONU: ")
print ("\n\n")



#faz login
login1 = f'LOGIN:::CTAG::UN={user},PWD={password};'
s = socket(AF_INET, SOCK_STREAM)
s.connect((server , 3337))
s.send(login1.encode())
time.sleep(1)


#ler o arquivo .CSV
csv_onu = 'onu.csv'

"""
FORMATO QUE DEVERA ESTAR O ARQUIVO onu.csv

Device Name,Device Type,Slot Number,PON Number,ONU Number,Physical Address,IP OLT
USUARIO TESTE1,AN5506-01-A1,1,1,5,FHTT11961234,IP_DA_OLT
USUARIO TESTE2,AN5506-01-A1,1,1,6,FHTT11711234,IP_DA_OLT
USUARIO TESTE3,AN5506-01-A1,1,1,7,FHTT11801234,IP_DA_OLT
USUARIO TESTE4,AN5506-01-A1,1,1,8,FHTT11911234,IP_DA_OLT
"""

with open(csv_onu, 'r') as csv_f:
    csv_reader = csv.reader(csv_f)
    next(csv_reader)
    for line in csv_reader:
        slot = line[2]
        port = line[3]
        mac = line[5]
        olt = line[6]
        remove_vlan(olt, slot, port, mac, vlan, s)
        adiciona_vlan(olt, slot, port, mac, vlan, s)
       
