### Types of XSS

* XSS happens when scripts run on a victim's browser when a website cant tell the difference betweene user input and website code.
* Stored XSS - When user input is stored on a server and retrieved later unsafely.
    * Although they weren't properly sanitized being injected, scripts could be escaped/sanitized if it was being retrieved 
    * Most dangerous type of XSS
    * <script> alert('XSS by Vickie'); </script>
    * Cookies and personal info could be stolen with XSS. But it can also change site contents and redirect to other sites.
 * Blind XSS - a stored XSS that takes place someplace else in the application.
    * Harder to detect, you cant find them by lookinh got reflected input from the server.
    * Attacks can host their own server and if they see a response to that server, then that web application has that XSS vulnerability.
 *
