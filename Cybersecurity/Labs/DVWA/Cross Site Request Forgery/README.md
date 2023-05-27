### Security Level: LOW
#
* For this attack, we'll host a HTML page that will change the admin's password if they were to visit the page.
* This page will be hosted on the same server that is running the web application.
* This doesn't have any access control (checking the origin site) or authorization (cookies) mechanisms to protect the 
  user from social engineering attacks, so it will be quite easy to change their password.
#
![](./images/CSRF_Low1.png)
![](./images/CSRF_Low2.png)

### Security Level: Medium
#
* This seem to have worked just fine with my previous HTML page, so I looked at the source code.
* Looks like there is some access control implemented to see if the connection comes from the same domain, which it does.
![](./images/CSRF_Medium1.png)
#
* So I tried hosting it somewhere different to see how I would circumvent this.
