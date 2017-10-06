#!/usr/bin/python2.7
import os
import time
import urllib2
from bs4 import BeautifulSoup

__version__ = 'clean_nodes v1'
__author__ = 'Riley'
__url__ = 'http://github.com/sadminriley'


'''
A script to scrape the puppetdash for unresponsive nodes,
and remove them from puppet and salt.

This script is meant to be ran on the puppetmaster server.
Enter your puppet url in the dash_url field below.
'''
dash_url = 'http://puppetdash.example.com/nodes/unresponsive'


def get_nodes():

    '''
    Using match to grab hostname strings for the unresponsive nodes,
    and urllib to open the dash url, and scrape it with bs4.
    '''
    nodes = []
    match = 'fqdn.com'
    page = urllib2.urlopen(dash_url)
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if link.string:
            # Checks end of line for match
            if link.string[-(len(match)):] == match:
                nodes.append(link.string)
                print link.string
    return nodes


def connect():
    '''
    Gets output from get_nodes function,
    and runs a a puppet cert clean and removes them from the salt-keys.
    '''
    for node in get_nodes():
        salt_remove = 'sudo salt-key -d %s -y' % node
        puppet_deactivate = 'sudo puppet node deactivate %s' % node
        try:
            os.system(salt_remove)
            time.sleep(4)
            os.system(puppet_deactivate)
        except OSError:
            print('\n!!! Error! Could not run pupper cert clean %s' % node)
        else:
            print('\nDone!\n The following nodes' +
                  'have been removed-: %s' % (unrespsonsive_nodes))
        finally:
            puppet_run = "sudo puppet agent -t"
            os.system(puppet_run)

connect()
