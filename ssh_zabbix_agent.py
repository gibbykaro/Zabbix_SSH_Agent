#Zabbix agent

import paramiko




ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect('host')

stout = ssh_client.exec_command('')

print(stout)
