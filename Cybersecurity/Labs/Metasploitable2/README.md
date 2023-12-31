### Goals
* The purpose of this lab is to get some experience with reconnasance tools, scripts and exploit databases.
### Nmap results
* As expected from a vulnerable machine, it has way too many open ports. Plenty of them show OS/version info.
* FTP, SQL & services that involve some sort of authentication would be noteworthy targets.
#
![](./images/Metasploitable2nmap.png) 
### [CVE: 2011-2523, vsftpd 2.3.4 backdoor command execution](https://www.exploit-db.com/exploits/49757)
* A malicious backdoor was added into the download archives for this version of VSFTPD back then, and
  we can use it to get a shell.
#
![](./images/VSFTPD.png)
### FTP & SQL weak login credentials
* By running built-in nmap scripts, we can check if the system has weak or non-existant login credentials.
#
![](./images/FTPANON.png)
![](./images/SQLBRUTE.png)
#
### [CVE: 2010-2075, UnrealIRCd 3.2.8.1 - Backdoor Command Execution](https://www.exploit-db.com/exploits/16922)
* Another backdoor added to the service back then, just like the vsftpd one.
* Although no version number was footprinted, the IRC service only had one exploit related to it. Works with a bind payload.
#
### [Tomcat Ghostcat attack](https://www.rapid7.com/db/modules/auxiliary/admin/http/tomcat_ghostcat/)
* An attacker can read the contents of configuration and source code files of all webapps deployed on Tomcat.
#
### [CVE: CVE-2004-2687, DistCC Daemon Command Execution](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2687)
* Port allows for remote users to send commands without authorization checks.
#
