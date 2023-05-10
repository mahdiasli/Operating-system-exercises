from scapy.all import *


num_packets_received = 0
num_packets_sent = 0


def process_packet(packet):
    global num_packets_received
    if packet.haslayer(IP):
        num_packets_received += 1


target_ip = '192.168.1.1'
ping_pkt = IP(dst=target_ip)/ICMP()
send(ping_pkt)


duration =  input()

duration = int(duration)

start_time = time.time()
while time.time() - start_time < duration:
    sniff(prn=process_packet, timeout=1)  
    num_packets_sent += 1
    ping_pkt = IP(dst=target_ip)/ICMP()
    send(ping_pkt)


print(f"Received packets : {num_packets_received}")
print(f"Sent packets : {num_packets_sent}")
