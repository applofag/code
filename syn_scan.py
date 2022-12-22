import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.CRITICAL)
from scapy.all import *
conf.verb = 0
if len(sys.argv) < 2:
    print("\nUsage:\n python syn_scan.py 192.168.50.1/24(CIDR notation)\n")
    sys.exit()
ip_range = sys.argv[1]
try:
    print("scanning " + ip_range)
    packets = IP(dst=ip_range)/TCP(dport=80,flags="S")
    for packet in packets:
        #print(packet.dst)
        ans,unans = sr(packet,timeout=0.1)
        ans.summary( lambda x : x[1].sprintf("%IP.src% is alive") )
except KeyboardInterrupt:
    exit()
