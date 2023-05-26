* Use this command to install java 17 JDK so that burp suite can run: **sudo apt-get install openjdk-17-jdk**
* On Firefox, scroll down in Settings under General to find Network Settings. For manual proxy configuration,
  set HTTP Proxy to 127.0.0.1 and Port 8080. Check off the box that uses it for HTTPS connections too.
* Go to http://burp/ to download the cert. Go to Settings, then Privacy and Security, scroll down to Certificates and
  click View Certificates. Import the downloaded cert and allow the cert to identity websites only.
