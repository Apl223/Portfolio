### Goals
* The purpose of this lab is to get some experience with reconnasance tools, scripts and exploit databases.
* I wanted to try to find at least one vulnerability that I can open a shell on.
### Nmap results
* As expected from a vulnerable machine, it has way too many open ports, and plenty of them show OS/version info.
* FTP, SQL & services that involve some sort of authentication would be noteworthy targets.
#
![](./images/Metasploitable2nmap.png) 
### [vsftpd 2.3.4 backdoor command execution](https://www.rapid7.com/db/modules/exploit/unix/ftp/vsftpd_234_backdoor/)
* Somehow, a malicious backdoor was added into the download archives for this version of VSFTPD back then, and
  we can use it to get a shell.
#
![](./images/VSFTPD.png)
