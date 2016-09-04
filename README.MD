#DESCRIPTION
**BADPROXY** is inspired by the talk [Owning Bad Guys {& Mafia} with JavaScript Botnets](https://media.blackhat.com/bh-us-12/Briefings/Alonso/BH_US_12_Alonso_Owning_Bad_Guys_WP.pdf) from [DEFCON 20 and Blackhat USA 2012](https://media.blackhat.com/bh-us-12/Briefings/Alonso/BH_US_12_Alonso_Owning_Bad_Guys_WP.pdf), which essentially talks about proxies’ ability to modify contents on the fly. It completely automates things the author has shown. Though it has been years, use of proxies is still widespread- for anonymity. The answer to anonymity still suggests using proxies- [so does Google](https://lmgify.com?q=how+to+become+anonymous). Using proxies may open door to a wide range of attack surface. Unless the connection is encrypted, a proxy server can easily *add/edit/delete* contents of requested resources- HTTP requests/responses. In fact, it is what a proxy is designed for.

BADPROXY, beside automation, also provides ability to work along side [**BeEF**](https://github.com/beefproject/beef). It also integrates [QRLJacking](https://www.owasp.org/index.php/Qrljacking), which requires little help from users of course. The best of all, it allows you to serve **RAT** instead of intended exe.

Though it has been developed specifically for **Debian**, basic setup are same for all Linux distributions. The actual commands, however, may differ slightly, please update it accordingly to suit your needs.  

**Features**:  
BADPROXY provides both Command Line & Graphical User Interface. The basic work-flow starts with CLI mode, where one can  
- Setup a proxy server which installs and/or configures SQUID  
- Work along side BeEF  
- Start GUI interface  
**Using GUI interface one can**  
- READ Keylogs  
- Update JavaScript being injected  
- Enable/disable RAT Infection  
- Inject QRLJacking phishing ads  
- Inject Google Analytics  


**License**:  
Read the [LICENSE](license) file copyright information.


#INSTALLATION
**Requirements**:  
The followings are required to be able to run BADPROXY;  
- Python  
- PHP  
- Apache  

**Supported platforms/languages**:  
The followings are supported platforms and/or languages;  
- Debian linux  
- PHP  
- Python  


#USAGE
Download the tool from the github
> git clone https://github.com/NCnew/BadProxy.git  

# Run the $./setup.py file with root permission  
![Run ./setup.py](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_001.png "Install the tool with ./setup.py")

**Script will check the required dependencies and ask with Y/N to install the required dependencies**

# Configurion  
   By defult tool will configure the squid proxy at port 8080, if you want to change the post then you can answer Y and do so.
   If you are good with the squid configuration you can change all other options of squid.conf file.(Be careful if you are not used to it)

   ![Select Y to change port ](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_002.png "Click Yes to configure the port number defult is 8080")


# Options
```
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
	***We recommended  to go to start GUI for easy access give input 4.***

   ![Select options for accorindg to requred function ](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_005.png "Click anyone one of the input for the options")


# To access the gui http://127.0.0.1/badproxy/index.php
    Username and password by defult will be badproxy:badproxy  
   ![Login to the dashboard to see further options ](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_006.png "Login with username and pass badproxy:badproxy")


```
    The GUI do have following features
    - READ Keylogs  
    - Update JavaScript being injected  
    - Enable/disable RAT Infection  
    - Inject QRLJacking phishing ads  
    - Inject Google Analytics  
    - List installed plug-ins on victim's browser  
```

# Features
  ![Features availabe form attack) ](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_007.png "Features avilabe for attack")


# Enable/disable RAT Infection
  ![Login to the dashboard to see further options (Execute replace with the RAT) ](https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_008.png "Replace all executable with RAT")


# Update JavaScript being injected  
  ![Login to the dashboard to update the javascript accorinding to your will ] (https://github.com/NCnew/BadProxy/blob/master/proxyboard/images/screenshot/Selection_009.png "All the update JavaScript form the dashboard will be injected to viticm browser")

```
***Comming soon feature list**
1.Extension backdoor injection
2.Backdoor Factory
3.GUI map of vitcim ip
4.Database to store the ip list and capture details.

Many more ...

```

# Author

[Nabin Kc](@CNew) &
[Prakash Sharma](@1lastBr3ath)

Information Security Researcher


**QRLJACKING**  
QRLJacking or Quick Response Code Login Jacking is a simple social engineering attack vector capable of session hijacking affecting all applications that rely on “Login with QR code” feature as a secure way to login into accounts. In a simple way, In a nutshell victim scans the attacker’s QR code results of session hijacking.

**Enable/Disable RAT infection**

Proxy will replace all the executable content with the back-door rat executable.
