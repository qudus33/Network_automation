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
    print("[+] Backing up {} to tftp server".format(devices['host']))
    net_connect = ConnectHandler(**devices)
    config_name = "{}.config".format(devices['host'])
    commands = [
        ['copy running-config tftp:', r"Address or name of remote host \[\]\?"],
        ['192.168.1.25', r"Destination filename \[[\w-]+\]\?"],
        [config_name, '']
    ]
    
    print(net_connect.send_multiline(commands))
    print("Job Done.")
    net_connect.disconnect()
    print("#" * 100)
