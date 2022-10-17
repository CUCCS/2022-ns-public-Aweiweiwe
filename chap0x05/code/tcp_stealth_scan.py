
from scapy.all import *

src_port = RandShort()
dst_ip = "172.16.111.110" 
dst_port = 80

resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)

if resp is None:
    print ("Filtered")

elif(resp.haslayer(TCP)):
    if (resp.getlayer(TCP).flags == 0x14):
        print ("Closed")
    elif(resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
        print ("Open")
