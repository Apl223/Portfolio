### Security level: LOW
#
* Got stuck on this because I was submitting the word "success" as instructed,
  but it kept telling me that the token was invalid. Which confused me because why would it be?
* After doing a some research, a value is generated on the basis of encoding the phrase with ROT13, and
  encoding that value with MD5 in the source code. That is then compared to the hidden token value.
  Since the hidden token isn't the right value, we have to figure out what the MD5 value is for "success" then replace the hidden
  token value with that, then proceed to submit the phrase "success".
    * Text-to-ROT13 converters and MD5 hash generators online were used.
#
![](./images/JavaScript_Low1.png)
![](./images/JavaScript_Low2.png)
#
