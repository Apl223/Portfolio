### Security Level: Low
#
* For this attack, we'll host a HTML page that will change the admin's password if they were to visit the page.
* **This page will be hosted on the same server that is running the web application.**
* This doesn't have any access control (checking the origin site) or authorization (cookies) mechanisms to protect the 
  user from social engineering attacks, so it will be quite easy to change their password.
#
![](./images/CSRF_Low1.png)
![](./images/CSRF_Low2.png)

### Security Level: Medium
#
* This seem to have worked just fine with my previous HTML page, so I looked at the source code.
* **Looks like there is some access control implemented to see if the connection comes from the same domain (192.168.1.8/test/testscript.html), which it does.**
#
![](./images/CSRF_Medium1.png)
#
* So I tried hosting it somewhere different to see how I would circumvent this.
* I uploaded the HTML page to this repository and accessed it as a GitHub page so it could render the HTML:
[https://apl223.github.io/Portfolio/Cybersecurity/Labs/DVWA/Cross Site Request Forgery/Test pages/testscript.html](https://apl223.github.io/Portfolio/Cybersecurity/Labs/DVWA/Cross%20Site%20Request%20Forgery/Test%20pages/testscript.html)
* As expected, I got the "That request didn't look correct." error.
* I would somehow have to preserve the referrer header as the same as the DVWA host in the request when a user makes a request from my HTML page,
  otherwise the password change will not work. This will most likely involve a layered attack with open redirection or XSS
  to grab that information before I can submit a password change.
* **<<span>meta> elements wont work to remove the requirement of the referrer header since the php source code requires we have it.**
    * Example: <<span>meta name="referrer" content="never"> 
* **Also tried circumventing the referrer check by putting 192.168.1.8 in different parts of the URL with history.pushState(), that didnt work either.**
* One solution was to copy the referrer header that is sent by clicking the "Change" button on the DVWA page to the
  HTTP request that comes from my HTML page. But this is suppose to be a social engineering attack that is supposed to be done on my HTML
  page instead of some MITM that would require a cert to be installed on the victim's browser.
* Although it doesnt involve my HTML page, **the best way would be to find a XSS vulnerability to carry out our CSRF. We can be compliant with the referrer by doing this.**
  Going back to the XSS lab, we can change the admin's password by inserting <img<span>><<span>img src="/dvwa/vulnerabilities/csrf/?password_new=pswd&password_conf=pswd&Change=Change">
  into the name field. We can confirm the password was changed via the HTTP responses.
  #
  ![](./images/CSRF_Medium2.png)
  #
  * As a note. the broken image symbol confirms that the <img<span>> element has been formed. Also meaning it wasn't escaped properly.
  ![](./images/CSRF_Medium3.png)
  #
  * **But this would be hard to pull off in practice because it would require the user to paste that into said form. Unless you have their session cookie, you could do it yourself.**
  * **It would also be difficult to change someone's password because most sites will require you to provide the current or previous password before changing it.**
  * **The biggest takeaway from this is that when access control comes into play, the best way to do a CSRF attack would be an XSS attack or a stored file on the vulnerable web application server.**
    You could look into [Same-Origin Policy Vulnerabilities](https://github.com/Apl223/Portfolio/blob/main/Cybersecurity/Books/BugBountyBootcamp/Same-Origin%20Policy%20Vulnerabilities/README.md) for some other possibilities.
  #
  ### Security Level: High
  #
  * This will require me to add the user token to my XSS that appears in the requests for the password change from the DVWA page.
    But since my HTML page can't be compliant with the referrer header, I'll have to do this from the same host.
  * I've attempted to go back to the XSS (Stored) page on the same security level and enter this into the name field with no alerts popping up:
   <img<meta>><<meta>img onload=alert(1) src="/dvwa/vulnerabilities/csrf/?password_new=pswd&password_conf=pswd&Change=Change">
  * Instead of using the <img<meta>> tag, I did **<body<meta>><<meta>body onload=alert(1) src="/dvwa/vulnerabilities/csrf/?password_new=pswd&password_conf=pswd&Change=Change">**
    which seems to have worked and an alert window shows, but no requests are made to the /csrf/ location on Burp.
  * <body<meta>><<meta>body onload=alert(1)><<meta>img src="/dvwa/vulnerabilities/csrf/?password_new=pswd&password_conf=pswd&Change=Change"> makes requests to /csrf/, but it doesn't change the password.
