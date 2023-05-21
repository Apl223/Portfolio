### Security level: LOW
# 
* Since this is in an extremely vulnerable state, we test it with a basic <script> tag with an alert function.
#
![](./images/XSS_S1.png)
![](./images/XSS_S2.png)
#
* It was saved onto the website, as we can see from the source code.
#
![](./images/XSS_S3.png)
![](./images/XSS_S4.png)
#
* Whenever I reload the page, it would repeat the alert and create more entries onto the guestbook. To avoid
  this, I would need to clear it via the form button.
#
![](./images/XSS_S5.png)
#
### Security level: MEDIUM
# 
* Changing capitilization for tags didnt work, such as <scrIPT> alert('hello') </script>
* Found some patterns to the sanization, or where characters are being escaped.
#
![](./images/XSS_S1LVL2.png)
#
* Nothing was sanizated with <body<meta> onload=alert(1)><meta> but no alerts appeared on screen.
#
![](./images/XSS_S2LVL2.png)
#
