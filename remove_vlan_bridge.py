import time

#função para remover a vlan da ONU
def remove_vlan(olt, slot, port, mac, vlan, s):
    s.send(f'DEL-LANPORTVLAN::OLTID={olt},PONID=NA-NA-{slot}-{port},ONUIDTYPE=MAC,ONUID={mac},ONUPORT=NA-NA-NA-1:CTAG::CVLAN={vlan},CCOS=0;'.encode())
    time.sleep(1)      
    rcv = s.recv(8192)

    if 'object not exist' in rcv.decode():
        print ("Erro ao remover VLAN na ONU " + mac )


    else:
        print("Sucesso ao remover a VLAN na ONU " + mac)

