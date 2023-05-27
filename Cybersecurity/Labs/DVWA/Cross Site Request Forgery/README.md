### Security Level: LOW
#
* For this attack, we'll host a HTML page that will change the admin's password if they were to visit the page.
* This page will be hosted on the same server that is running the web application.
* This doesn't have any access control (checking the origin site) or authorization (cookies) mechanisms to protect the 
  user from social engineering attacks, so it will be quite easy to change their password.
#


