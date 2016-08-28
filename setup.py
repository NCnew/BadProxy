#!/usr/bin/python

try:
  from include.functions import Call, CheckInet, CheckServer, CheckUser, Configure, Input, Install, Options, PackageManager, Quit
except:
  print '[i] Couldn\'t find required libraries ..'
  exit()

BANNER = '''
/************************************************************************
 *                                                                      *
 *                          BADPROXY v1.0                               *
 *                Nabin (@c_New) & Prakash (@1lastBr3ath)               *
 *                                                                      *
 ************************************************************************/
 '''

print BANNER

print '[+] Checking user- requires running as root: %s' % (CheckUser(), )
print '[+] Checking Internet - requires Internet connectivity: %s' % (CheckInet(),)
print '[+] Checking Apache- if installed'
if CheckServer() == None:
  Quit('[!] Sadly, we currently only support Apache\n[~] Please install Apache first')


print '[+] Checking SQUID- if already installed ..'
if Call(['which','squid']):
  opt = Input('[-] SQUID NOT Found !!\n[i] Install? (Y/n) ')
  if opt.upper() == 'Y':
    print '[+] Checking Package Manager ...'
    packman = PackageManager()
    print '[+] Using Package Manager: %s' % (packman, )

    if packman != 'apt-get':
        Quit('[?] What should I do now?')

    print '[+] Checking SQUID- if available under %s' % (packman, )

    if not Call(['apt-cache','show','squid']):
      print '[+] Found !!\n[!] Installing SQUID via %s' % (packman, )
      Install()

    if not Call(['which', 'squid']):
      opt = Input('[!] Installation completed !!\n[i] Configure? (Y/n) ')
      if opt.upper() == 'Y':
        Configure()
      else:
        Options()
  else:
    Quit('[?] I don\'t know what I else I\'m supposed to do now :(')
else:
  opt = Input('[!] Already installed !!\n[i] Configure? (Y/n) ')
  if opt.upper() == 'Y':
    Configure()
  else:
    Options()
