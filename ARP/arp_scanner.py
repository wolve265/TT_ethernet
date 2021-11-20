from scapy.all import srp,Ether,ARP

def scan_arp(ip):
    arp_r = ARP(pdst=ip)
    br = Ether(dst='ff:ff:ff:ff:ff:ff')
    request = br/arp_r
    answered, unanswered = srp(request, timeout=1)
    print('\tIP\t\t\t\t\tMAC')
    print('_' * 37)
    for i in answered:
        ip, mac = i[1].psrc, i[1].hwsrc
        print(ip, '\t\t' + mac)
        print('-' * 37)


if __name__ == "__main__":
    scan_arp("192.168.0.0/255")
