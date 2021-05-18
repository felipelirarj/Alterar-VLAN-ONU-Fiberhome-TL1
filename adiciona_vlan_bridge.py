import time

#função para adicionar a vlan da ONU
def adiciona_vlan(olt, slot, port, mac, vlan, s):
    s.send(f'CFG-LANPORTVLAN::OLTID={olt},PONID=NA-NA-{slot}-{port},ONUIDTYPE=MAC,ONUID={mac},ONUPORT=NA-NA-NA-1:CTAG::CVLAN={vlan},CCOS=0;'.encode())
    time.sleep(1) 
    rcv = s.recv(4096)
  
    if 'object not exist' in rcv.decode():
        print ("Erro ao adicionar VLAN na ONU " + mac )

    else:
        print("Sucesso ao adicionar a VLAN na ONU " + mac)
