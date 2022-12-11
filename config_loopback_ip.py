# This scrip configure the loopback ip using the value of the 4th octet of the ip
import netmiko
from netmiko import ConnectHandler
import re

address_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
loopback_list = []
for ip in address_list:
    pattern = r"([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)"
    result = re.search(pattern, ip)
    loopback_ip = f"{result[4]}.{result[4]}.{result[4]}.{result[4]}"
    loopback_list.append(loopback_ip)
loopback_interface_increamnet = 0
for ip in address_list:
    host = ip
    username = 'qudus'
    password = 'cisco'

    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**device)
    commands = [
        'config t', 
        'interface lo0', 
        f'ip address {loopback_list[loopback_interface_increamnet]} 255.255.255.255',
        'end'
    ]
    net_connect.send_config_set(commands)
    print(net_connect.send_command('show ip int brief'))
    print("*" * 100)
    loopback_interface_increamnet += 1
    net_connect.disconnect()