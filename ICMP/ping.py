from icmplib import multiping

list_of_ip = ['192.168.0.206', '192.168.0.31']
hosts = multiping(list_of_ip)

for host in hosts:
    if host.is_alive:
        print(f'{host.address} is up!')
    else:
        print(f'{host.address} is down!')
