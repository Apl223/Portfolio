### Security level: LOW
#
* Escaped from the expected command with an & symbol to start the Windows calculator
  application on the virtual machine the web application is running on. Easy test with
  the application set to being very vulnerable.
#
![](./images/CommandInjection_Low1.png)
![](./images/CommandInjection_Low2.png)

### Security level: MEDIUM
#
* Looking at the source code, they only sanitize && and ; to empty strings. 
* Therefore, our previous command injection on LOW works just the same.
#
![](./images/CommandInjection_Medium1.png)
#

### Security level: HIGH
#
