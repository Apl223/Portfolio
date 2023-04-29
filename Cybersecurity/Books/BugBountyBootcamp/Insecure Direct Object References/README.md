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
