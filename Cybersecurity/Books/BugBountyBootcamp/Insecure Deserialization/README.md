### Insecure Deserialization
#
* Happens when an application deserializes objects without proper precuation. Attackers can change how objects behave.
  This usually involves abusing functions that are vulnerable.
* Hard to find & exploit. But can be used for RCE.
* **Serialization** allows for bits of data to be formated in a way that can be saved to a database or transfered across a network.
* **Deserialization** reads the serialized object from a file or network and converts it back.
* PHP, Java, Python, and Ruby support both of these.
* These help avoid corruption when sending pakcets or storing data.
* This attack arises when an attackers can manipulate an object to cause unintended consequences. 
  They can use it to authenticate as someone else or bypass it.
 ### Prevention
 #
 * Difficult and varies based on programming language.
 * Proper checks, use an allowlist for certain classes if deserialization is neccasary.
 * Simpler data types than classes (strings,arrays,etc)
 * Prevent cookie tampering by keeping state on servers instead of user input for session information.
 * Make sure dependencies are up to date via third party code. Or remove classes altogether.
 ### Hunting for ID
 #
 * Source code review. Check if classes are accepting user input recklessly.
     * PHP: unserialize()
     * Java: readObject()
     * Python: pickle.loads()
     * Ruby: Marshall.load()
 * You could find them without the source code. Look for large blobs of data passed into an application.
     * Large base64 strings that could have serialized objects
 * Seek features that are prone. Some involve deserializing user supplied objects likke database inputs, authentication tokens,
   and HTML parameters. You'll then have to figure out if its a Python or PHP object.
 * ID can be limited to obscure entry points, lack of privledge, or unavailable to unauthorized users.
