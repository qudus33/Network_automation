# Generate device login details from lists of ip address
import json
import netmiko
from netmiko import ConnectHandler

address_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
device_list = []
username = 'qudus'
password = 'cisco'

for ip in address_list:
    device = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': username,
            'password': password
        }
    device_list.append(device)

for devices in device_list:
    print(devices['host'])
print(device_list)
json_formatted = json.dumps(device_list, indent=2)
print(json_formatted)

# for device in device_list:
#     print(f"Connecting to device {device['host']}")
#     net_connect = ConnectHandler(**device)
#     print(net_connect.send_command('show ip int brief'))
#     print("*" * 100)
#     net_connect.disconnect()