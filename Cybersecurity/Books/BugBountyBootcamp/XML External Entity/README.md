### XML External Entity
#
* Targets XML parsers. Leads to SSRFs and DoS attacks.
* XML is designed for storing and transporting data. It allows you to define data
  structures in text format using tree-like structures such as HTML. Its commonly used for SAML.
* Also used in authentication, file transfers, image uploads or HTTP data.
* XML docs have a document type definition (DTD) that defines the data & structure of the doc.
* The DOCTYPE tag is used for this. They can be loaded externally/internally.
* <! ENTITY file "Hello">
    * This XML entity will load the value of file. Entities are referenced to and load whatever variable is in them.
    * Attacks can use these for info disclosures and more. They could use them to reference external sources, 
      like a web server hosted by the attack to send back a payload for blind attacks. Like a reverse TCP connection.     
* Sites could use older or poorly configured XML parsers.
* You could upload files too:
    *  <! ENTITY file SYSTEM "fil<meta>e://etc/shadow">, where you can read passwords on Unix systems
### Prevention
#
* Disable or limit DTD processing on parsers. Disable params or external entities if needed. Limit parse time and depth.
  Or disable expansion of entities altogether.
* Allowlists, sanitization, or less complex data formats like JSON, disable outbound network traffic and disable dependencies
### Hunting for XXEs
#
* Look into HTTP messages for XML strings like <?xml. You may have to decode blocks of data in base64 or some other common encoder.
* Look for file upload features. XML forms many file types and metadata within images are based on XML.
* You could try to force apps to process XML in the Content-Type header on a HTTP message.
* Read leaked info from server responses for classic attacks. You could use PUBLIC instead of SYSTEM. Extract common system files.
* Hide your payload in different payloads, like svg images or word docs. File endpoints may not have the same protections as regular endpoints.
* You may not be able to edit HTTP messages, but you can still pass user input.
