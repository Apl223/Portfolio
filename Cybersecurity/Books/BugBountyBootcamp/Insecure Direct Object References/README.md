### Insecure Direct Object References
#
* IDOR involes accessing resources that do not belong or were not meant to be accessed to you. Usually done by changing URL parameters like user_id, file names or numbers. You could access someone's private messages by changing the ID parameter such as ?user_id=1233.
* Predictable naming conventions are a source for IDOR.

### Prevention

* Randomize object names
* Authorization. Check user's identity & permissions
* Hashing

### Hunting IDORs

* Create multiple accounts & discover as many features as possible.
* Use a proxy to modify packets. REST & GraphQL are often vulnerable to this.
* Decode encoded or hashed IDs. Common encoding schemes: base64, URL encoding, base64url or use Smart Decode tool. 
* Sometimes there isn't enough entropy in randomization.
* Use API endpoints to retrieve IDs.
* Applications usually use cookies, not IDs. But you could try inserting one anyway.
* Blind IDORs dont leak info directly, but from somewhere else. These could be used to find vulnerabilities elsewhere.
* Access controls may not work the same for all request methods. So while GET may not work, DELETE could.
* You may also change the filetype like ?receipt_id=2983.json becuase the application may treat those with different access controls, even if those files dont use the .json extension.
* Focus on state-changing features for maximum severity. Write based IDORs like password resets/changes, account recovery, and so on. Or Read-based IDORs that leak info such as direct messages or personal info.
