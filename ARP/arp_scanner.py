from scapy.all import srp,Ether,ARP,conf

def scan_arp(ip):
    print("Scanning...")
    conf.verb = 0 # verbose disable
    arp_r = ARP(pdst=ip)
    br = Ether(dst='ff:ff:ff:ff:ff:ff')
    request = br/arp_r
    answered, _ = srp(request, timeout=1)
    print(f"IP \t\t\t MAC")
    for i in answered:
        ip, mac = i[1].psrc, i[1].hwsrc
        print(ip, '\t\t', mac)


if __name__ == "__main__":
    scan_arp("192.168.0.0/24")
