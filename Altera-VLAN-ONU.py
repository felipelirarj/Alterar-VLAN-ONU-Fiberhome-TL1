import csv
from socket import *
import time

print ('Sistema de alteração de VLAN em massa via Planilha .CSV\n\n')

## ip do anm/unm, user e senha TL1, vlan e ip da olt

server = input ("Informe o IP do servidor UNM2000: ")
user = input ("Informe o login administrador: ")
password = input ("Informe a senha do administrador: ")
olt = input ("Informe em qual OLT a planilha pertence: ")
vlan = input ("Informe a VLAN a ser adicionada à ONU: ")
print ("\n\n")


#faz login

login1 = f'LOGIN:::CTAG::UN={user},PWD={password};'
s = socket(AF_INET, SOCK_STREAM)
s.connect((server , 3337))
s.send(login1.encode())
time.sleep(1)


#função para remover a vlan da ONU
def remove_vlan(slot, port, mac):
   s.send(f'DEL-LANPORTVLAN::OLTID={olt},PONID=NA-NA-{slot}-{port},ONUIDTYPE=MAC,ONUID={mac},ONUPORT=NA-NA-NA-1:CTAG::CVLAN={vlan},CCOS=0;'.encode())
   time.sleep(1)      
   rcv = s.recv(8192)

   if 'object not exist' in rcv.decode():
    print ("Erro ao remover VLAN na ONU " + mac )

   else:
    print("Sucesso ao remover a VLAN na ONU " + mac)

   
#função para adicionar a vlan da ONU
def adiciona_vlan(slot, port, mac):
  s.send(f'CFG-LANPORTVLAN::OLTID={olt},PONID=NA-NA-{slot}-{port},ONUIDTYPE=MAC,ONUID={mac},ONUPORT=NA-NA-NA-1:CTAG::CVLAN={vlan},CCOS=0;'.encode())
  time.sleep(1) 
  rcv = s.recv(4096)
  
  if 'object not exist' in rcv.decode():
    print ("Erro ao adicionar VLAN na ONU " + mac )

  else:
    print("Sucesso ao adicionar a VLAN na ONU " + mac)

   

#ler o arquivo .CSV
csv_onu = 'onu.csv'

with open(csv_onu, 'r') as csv_f:
    csv_reader = csv.reader(csv_f)
    next(csv_reader)
    for line in csv_reader:
        slot, port, indice, mac = line[2:6]
        remove_vlan(slot, port, mac)
        adiciona_vlan(slot, port, mac)


       
