#!/usr/bin/python
from argparse import ArgumentParser
from smtplib import SMTP
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

def cron(cronstring):
    '''
    Function to create a cronjob using pycron
    '''
    pass

def send_email(username, password):
    '''
    Function to send an email. Must pass username and password
    '''
    sendmail = SMTP()
    sendmail.connect('mail.google.com')
    sendmail.login(username, password)
    from_addr = 'serversemail@hostname.com'
    to_addr = 'recipient@hostname.com'
    subject = raw_input('Please enter the subject of your email-:\n')
    msg = raw_input('Please enter the message you would like to send-:\n')
    sendmail(from_addr, to_addr, subject, msg)

def main():
    '''
    Arguments
    '''
    parser = ArgumentParser()
    parser.add_argument('-e',
                        help='Execute a remote command on a server',
                        dest='execute'
                        )

