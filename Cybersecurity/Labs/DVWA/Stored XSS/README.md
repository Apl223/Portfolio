### Security level: LOW
# 
* Since this is in an extremely vulnerable state, we test it with a basic <script> tag with an alert function.
#
![](./images/XSS_S1.png)
![](./images/XSS_S2.png)
#
* It was saved onto the website, as we can see from the source code.
* To avoid adding more entries to the guestbook, I would need to clear it via the form button.
#
![](./images/XSS_S3.png)
![](./images/XSS_S4.png)
#
### Security level: MEDIUM
# 
* Changing capitilization for tags didnt work, such as <scrIPT> alert('hello') </script>
* Found some patterns to the sanization, or where characters are being escaped. Looks like <<meta>script> tags are being removed
#
![](./images/XSS_S1LVL2.png)
#
* <<meta>body> tags are being sanitized completely, such as <body<meta> onload=alert(1)><meta>.
#
![](./images/XSS_S2LVL2.png)
#
* At this point, it was time to look at the source code for any hints.
#
![](./images/XSS_S3LVL2.png)
![](./images/XSS_S4LVL2.png)
#
* It looks like the message text area strips any tags and adds slashes in the message after submission. Just like what we observed.
* But the name field doesn't have the same stringent rules for sanitization because it replaces <script> with an empty string.
  This means we can layer a <script> tag within another one so that it strips the inner one and and forms the outter <script> tag.
* We have an issue with writing the entire script line, so we inspect the name field and increase the **maxlength** attribute to 50 so we
  can insert <scri<script>pt>alert('hello')</script>
#
![](./images/XSS_S5LVL2.png)
#
### Security level: HIGH
#
* Looking at the source code, there seems to be another one to one conversion of a string to an empty string.
  I thought by changing some of the capitilizations of the letters for that same string it compares itself to, this might've not been
  that complicated to figure out. But the more requests I sent in, I realized it was a more complicated protection mechanism
  involving wildcard symbols (*) because <scri<script>pt>alert('hello')</script> was being filtered for the most part.
* This isn't enough to put together a complete exploit, but its a start. I had a hard time figuring out a solution so I seeked some solutions.
  The hints provided by the DVWA page says that I should use HTML events.
* **Looks like a previous piece of code I used for testing for the medium level problem works for this: <body<meta> onload=alert(1)><meta>.**
  I assumed this wouldn't work before since it didnt work on medium, but that goes to show that these vulernabilities don't work in that fashion where
  more complicated solutions neccasarily exploit simple issues.
#
![](./images/XSS_S1LVL3.png)                                                                     
#
