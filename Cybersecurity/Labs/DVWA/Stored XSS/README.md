### Security level: LOW

Since this is in an extremely vulnerable state, lets test if it will take a <script> tag with no sanitization:
  
![](./images/XSS_S1.png)
![](./images/XSS_S2.png)
* Looks like it was saved onto the website, as we can see from the source code.
![](./images/XSS_S3.png)
![](./images/XSS_S4.png)
* Whenever I reload the page, it would repeat the alert and create more entries onto the guestbook. To avoid
  this, I would need to clear it via the form button.
![](./images/XSS_S5.png)
# 
