# This scrip runs command with netmiko using the send_multiline_timing method.
import netmiko
from netmiko import ConnectHandler

address_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']

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
        'interface f0/1', 
        'shutdown',
        'end'
    ]
    net_connect.send_multiline_timing(commands)
    print(net_connect.send_command('show ip int brief'))
    print("*" * 100)
    net_connect.disconnect()