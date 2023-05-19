### Business Logic Errors & Broken Access Control
#
* Different from other vulnerabilities that involve sanitization problems. This takes
  advantage of misusing application logic to achieve unintended results.
* **Broken access controls happen when functions or resources aren't properly protected, 
  and logic errors are for when developers overlook misuse cases.**
      * Accessing admin panels, IDOR, SSRF are examples of broken access control. These
        could be found by tampering with cookies or request headers. Directory traversal is also
        an example of broken access control, but requires sanitization issues to occur.
* Multi-factor authentication has common logic errors where you can skip 
  process steps by visiting the URL of the last step.
* Another common problem with logic errors is multi-step checkout processes.
  If the app keeps track of new or saved credit cards in POST requests, you
  could try changing the saved credit card to a fake one and the app may not
  verify it if it assumes saved numbers as verified.
* Logic errors can manifest in many wars and most vulnerability scanners dont have the
  intelligence to understand application logic or business requirements.
### Prevention
#
* Verify if functions work as intended. Also requires knowledge of business
  requirements and the development process of the app.
* Make sure access control policies are accurate.
### Hunting for LE & BEC
#
* Some of the easiest bugs to find, it requires experimentation. Keep track of requests
  and how functionalities & access control behave to them.
* Modify parameters that could potentially have some misuse cases. As an example, change
  amounts charged in responses or requests and see how the app reacts.
