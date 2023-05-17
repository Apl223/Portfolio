### SQL Injections
#
* Similar to XSS, this executes incorrectly filtered or escaped SQL commands to an app's database.
* Leads to authentication bypass, data leaks, tampering and RCE.
* Login prompts are an avenue for these vulnerabilities since you are submitting queries for login information.

### Second-Order SQL Injections
#
* First order injections are when user input is used directly in a SQL query.
* Second order is when you retrieve stored user input from the database.

### Prevention
#
* Prepared statements/Parameterized queries. 
    * These make injections practically impossible by ensuring user input doesn't alter SQL logic.
    * The SQL servers compiles the SQL query before any user input is inserted. You'd define
    the logic first before the input data.
    * Anything that deviates from this logic will be treated as a string that is uncapable of executing.
* Create an allowlist for values. You could allow operators like ORDER BY for example.
* Escaping/Sanitizing.
    * ' and " should be fixed.
    * **Different databases have specific characters.**

### Hunting SQL Injections
#
* Categorized into classic & blind varieties.
* Common technique is to insert a single ' then for errors or odd behavior.
* The ' denotes the end of a query string.
* Introducing or experiencing time delays could be a hint.
* Fuzzing
* **Classic** - SQL queries that are returned directly to the attacker.
#
* **Blind** - Harder to find because the web app doesn't return SQL data or error messages. Also called **Inferential SQL injections**.
* These are normally boolean or time based.
* Boolean testing involves sending test conditions to recieve true/false return values. Infering info.
* Time-based injections rely on response times between different payloads. This is meant more for apps that dont give visual clues.

### NoSQL Injections
#
* Stands for Not-Only SQL. Does not use SQL.
* SQL stores data in tables. NoSQL stores data in key-value pairs and graphs.
* Syntax is database specific:
    * MongoDB: Users.find({username:'vickie',password:'password123'})
    * Replace 'password123' with {$ne: ""}. This searches for a paired value that does equal " ". You can find passwords this way.
    * You can execute JavaScript as well. $where,mapReduce,$accumulator, and $function.
    * Characters like ' , ", ; , \ , () , [] , and {} can be used.
### Prevention
#
* Validators
* Disable server-side JavaScript with --noscripting on the CMD.
* Disable security.javascriptEnabled on the config file.
* **Principle of least priviledge** - only give apps the priviledges they need.

### Enumerating the service
#
* @@version on Microsoft SQL server & MySQL
* v$version for Oracle.

### Gain a web shell
#
* <<meta>? system($_REQUEST['cmd']); ?>
* Create a file onm the server with a nonexistant user:
    * SELECT Password FROM Users WHERE Username='abc'
      UNION SELECT "<? system($_REQUEST['cmd']); ?>"
      INTO OUTFILE "/var/www/html/shell.php"
    * Password is blank, so you can upload that cmd script then visit that scripts URL to execute it.
        * <span>http://www.example.com/shell.php?cmd=COMMAND
