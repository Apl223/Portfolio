### Template Injection
#
* Also called server-side template injection (SSTI)
* These **target template engines**. These combine app data and web templates to produce web pages with dynamic content/
* Jinja2 is a template engine that runs on Python. 
* Some enviroments have sandboxes to mitigate this vulnerability.
* Web templates/template engines seperate server-side app logic and client-side presentation code.
* In Jinja {{ }} is interpreted as a Python expression (variable or function that returns a value).
  {% %} is interpreted as a statement (code that doesn't return a value).
* Template files look like HTML files with HTML headers and elements. But code indicating where Python is ran.
* You can also have Python scripts read Jinja files and product the HTML page.
* Template engines allow devs to be more effecient by supplying different data sets and reusing templates with them.
* **Injections in templates happen when devs treat them like strings and concatenate user input into them.** Similar to SQL injections.
* If the template engine can't tell where user-supplied data ends & template logic starts, it will take user input as template code.
### Prevention
#
* Patching & updating frameworks and libraries your templates use. 
* Sandboxes to mitigate the vulnerability.
### Hunting for SSTI
#
* Endpoints coincide with XSS attacks, so anything that can be supplied by the user.
* Test strings to generate errors:
    * PHP/Python: {{7*7}}
    * Java: ${7*7}
    * Ruby: <%=7*7 %>
    * [abcxx]
* If they returned the result, it means its part of the code.
* Go through each to test what engine it is, generate errors if needed.
* Try to use modules like {{os.system('ls')}}. If an error says it is "undefined"
  that means its not in the enviroment. These are not included so its easier to mitigate these attacks. __import()__ may not work either.
