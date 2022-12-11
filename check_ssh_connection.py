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
    print("Checking device with ip or hostame of {}".format(host))
    net_connect = ConnectHandler(**device)
    
    if net_connect.check_enable_mode() == True:
        print("Device with ip or hostname {} is reachable.\n".format(host))
        net_connect.disconnect()
    else:
        print("Device with ip or hostname {} is unreachable".format(host))
        