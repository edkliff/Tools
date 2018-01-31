from paramiko import SSHClient, SSHConfig, AutoAddPolicy
from os import path
from time import sleep
import telebot


bot_token = 'your bot token'
bot = telebot.TeleBot(bot_token)


""" Example of config """
servers_and_statuses = {
    'preprod': {
        'hostname': 'example.com',
        'elasticsearch': '',
        'redis-server': '',
        'rabbitmq-server': ''
    }
}


""" List of channels(chat_id) in telegram """
tm_channels = ('channel ID',)
""" How many times between status resolve? """
TIMER = 15


def get_service_status(hostname, servicename):
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_config = SSHConfig()
    config_file = path.expanduser("~/.ssh/config")
    if path.exists(config_file):
        config_file_opened = open(config_file)
        ssh_config.parse(config_file_opened)

    server_config = ssh_config.lookup(hostname)
    ssh_client.connect(hostname=server_config['hostname'],
                       username=server_config['user'],
                       port=server_config['port'],
                       key_filename=server_config['identityfile'])

    stdin, stdout, stderr = ssh_client.exec_command("sudo service {} status | grep 'Active'".format(servicename))
    stdout_file = stdout.read()
    status_line = stdout_file.decode()
    status = status_line.split()[1]
    ssh_client.close()
    return status


while True:
    for host in servers_and_statuses:
        host_name = servers_and_statuses[host]['hostname']
        services = servers_and_statuses[host].keys()
        for service in services:
            if service != 'hostname':
                service_status = get_service_status(host_name, service)
                if servers_and_statuses[host][service] != service_status and servers_and_statuses[host][service] != '':
                    print(host_name, service, service_status)
                    mess = '{} is {} now on {}'.format(service, service_status, host_name)
                    for chan in tm_channels:
                        bot.send_message(chan, mess)
                servers_and_statuses[host][service] = service_status
    # print(servers_and_statuses)
    sleep(TIMER)

