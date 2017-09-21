#!/usr/bin/python
import os
import smtplib
import subprocess
from paramiko import SSHClient, AutoAddPolicy


class SSH(object):
    '''
    Object to establish an ssh connection.
    from common import SSH
    host = 'yourhostname.com'
    ssh = SSH(host)
    commands = ['ls','cat file.txt']
    ssh.connect(commands)

    Special thanks to @angelokie for showing me how to make better objects,
    and the concept of creating re-usable python functions for other projects or tasks.
    '''
    client = SSHClient()
    def __init__(self, host, user='root', port=22, ssh_key='~/.ssh/id_rsa.pub', password=None):
        self.host = host
        self.user = user
        self.port = port
        self.sshkey = ssh_key
        self.password = password

    def connect(self, commands):
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(self.host, port=self.port, user=self.user, password=self.password)
        for command in commands:
            stdin, stdout, stderr = self.client.exec_command(command)
            for line in stdout.readlines():
                print line
                self.client.close()

class Cron(object):
    '''
    Class to set a cron job
    '''
    pass
