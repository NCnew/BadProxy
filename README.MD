#DESCRIPTION
**BADPROXY** was inspired by the talk [Owning Bad Guys {& Mafia} with JavaScript Botnets](https://media.blackhat.com/bh-us-12/Briefings/Alonso/BH_US_12_Alonso_Owning_Bad_Guys_WP.pdf) from DEFCON 20 and Blackhat USA 2012 which essentially talks about proxies’ ability to modify contents on the fly. What BADPROXY does is- completely automate things the author has shown. Though it has been years, use of proxies is still widespread- for anonymity. The answer to anonymity still suggests using proxies- [so does Google](https://lmgify.com?q=how+to+become+anonymous). Using proxies may hide your IP but it also opens door to a wide range of attacks. Unless the connection is encrypted, a proxy server can easily *add/edit/delete* contents of requested resources; both requests & responses.

BADPROXY, beside automation, also provides ability to work along side [**BeEF**](https://github.com/beefproject/beef). It also integrates [QRLJacking](https://www.owasp.org/index.php/Qrljacking) which requires little help from you of course. The best of all- it allows you to serve **RAT** instead of intended exe.

Though it has been developed specifically for **Debian**, basic setup are same for all Linux distributions. The actual commands, however, may differ slightly, please update it accordingly to suit your needs. If you've already installed squid which is below version 3, you might face difficulty making thigs work.

**Features**:  
BADPROXY provides both Command Line & Graphical User Interface. The basic work-flow starts with CLI mode, where one can  
\- Setup a proxy server which installs and/or configures SQUID  
\- Work along side BeEF  
\- Start GUI interface  
**Using GUI interface one can**  
\- READ Keylogs
\- Update JavaScript being injected  
\- Enable/disable RAT Infection  
\- Inject QRLJacking phishing ads  
\- Inject Google Analytics  


**License**:  
Refer to [LICENSE](LICENSE)


#INSTALLATION
**Requirements**:  
The followings must be preinstalled on your system for running BADPROXY;  
\- Python  
\- PHP  
\- Apache  


**Supported platforms/languages**:  
The followings are supported platforms and/or languages;  
\- Debian Linux  
\- PHP  
\- Python  


#USAGE
```
$ git clone https://github.com/NCnew/BadProxy.git
$ cd BadProxy/; sudo python setup.py
```
![Install](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_001.png "Install")

You'll be prompted for confirmation during setup.

# Configuration    
BADPROXY will setup squid proxy on port 8080, by default. However, you can configure it during configuration or you can also edit squid.conf directly, but, be careful, if you are not used to it.

 ![Configure](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_002.png "Configure")


# Options
```bash
	 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 + [1] Start SQUID (with Keylogger)                           +
	 + [2] Start SQUID alongside BeEF (*nix only)                 +
	 + [3] Manual configuration                                   +
	 + [4] Start GUI                                              +
	 + [5] RE-configure SQUID                                     +
	 + (Run the above options if you find any issue in injection) +
	 + [6] Stop BadProxy Server                                   +
	 + [H] HELP                                                   +
	 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                  	 Press ^C To EXIT  
	 >
```
![Start GUI](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_005.png "Start GUI")

To start GUI, enter `4` and browse to [http://127.0.0.1/badproxy/index.php](http://127.0.0.1/badproxy/index.php) with username/password `badproxy`.
![Login](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_006.png "Login")

![Features](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_007.png "Features")

**Enable/disable RAT Infection**    
  ![Toggle RAT Infection](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_008.png "Toggle RAT Infection")

**Update JavaScript being injected**    
  ![Update JavaScript] (https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_009.png "Update JavasCript")

**QRLJACKING**  
QRLJacking or Quick Response Code Login Jacking is a simple social engineering attack vector capable of session hijacking affecting all applications that rely on “Login with QR code” feature as a secure way to login into accounts. In a simple way, In a nutshell victim scans the attacker’s QR code results of session hijacking.

**Toggle RAT Infection**    
This will replace the content of executables with your provided RAT.

# TODO
1. Integrate Backdoor Factory
2. Employ map of infected machines
3. Integrate database to store IP and others
4. Integrade docker to support multiple OS

# Author

[Nabin Kc](@CNew) &
[Prakash Sharma](@1lastBr3ath)

Security researchers
