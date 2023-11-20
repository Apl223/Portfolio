This module involves looking for patterns to 
deduct user IDs. You could then change user settings
and make actions on their behalf. 

### Security level: LOW

* dvwaSession goes up by 1, so that corosponds to the admin account. Next would be a user

### Security level: MEDIUM

* dvwaSession increases in the last 3 digits based off time().> 

### Security level: HIGH

* dvwaSession is encoded with the md5 hash function then is set to expire with the time() function + 3600 seconds
