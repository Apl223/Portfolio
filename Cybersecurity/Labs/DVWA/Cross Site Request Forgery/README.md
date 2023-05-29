### Security Level: Low
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
#
![](./images/CSRF_Medium1.png)
#
* So I tried hosting it somewhere different to see how I would circumvent this.
* I uploaded the HTML page to this repository and accessed it as a GitHub page so it could render the HTML:
[https://apl223.github.io/Portfolio/Cybersecurity/Labs/DVWA/Cross Site Request Forgery/Test pages/testscript.html](https://apl223.github.io/Portfolio/Cybersecurity/Labs/DVWA/Cross%20Site%20Request%20Forgery/Test%20pages/testscript.html)
* As expected, I got the "That request didn't look correct." error.
* I would somehow have to preserve the referrer header in the request when a user makes a request from my HTML page,
  otherwise the password change will not work. This will most likely involve a layered attack with open redirection or XSS
  to grab that information before I can submit a password change.
* <<span>meta> elements wont work to remove the requirement of the referrer header since the php source code requires we have it.
    * <<span>meta name="referrer" content="never"> 
* One solution was to copy the referrer header that is sent by clicking the "Change" button on the DVWA page, to the
  HTTP request that comes from my HTML page. After doing a little bit of research, we can add refer heads with history.pushState().
