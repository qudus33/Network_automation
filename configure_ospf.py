import netmiko
from netmiko import ConnectHandler
from time import sleep

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
    net_connect = ConnectHandler(**devices)
    commands = [
        'config t',
        'router ospf 1',
        'network {} 0.0.0.0 area 0'.format(devices['host']),
        'end'
    ]
    net_connect.send_config_set(commands)
    net_connect.disconnect()

print("[+] Ospf configuration on routers completed")
print("[+] Waiting to show neighbor information")
sleep(60)    
for devices in device_list:
    net_connect = ConnectHandler(**devices)
    print("showing neighbor details for host {}".format(devices['host']))
    print(net_connect.send_command("show ip ospf neighbor"))
    net_connect.disconnect()
    print("*" * 100)
print("Done")