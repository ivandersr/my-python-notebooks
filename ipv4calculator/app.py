from classes.calcipv4 import CalcIPv4


calc_ipv4 = CalcIPv4(ip='10.1.1.25', mascara='255.255.255.0')

print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mascara}')
print(f'Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'Número de IPs: {calc_ipv4.num_ips}')
