### Cross Site Request Forgery

* You can send out HTTP requests to pretend to be the victim, and make unwanted actions on their behalf.
* Targets state-changing requests, like sending tweets or changing settings.
* These requests are authenticated with cookies. You could trick a user with a clickjack and have them tweet regardless of where the request is coming from since you are using their cookies

### Prevention

* CSRF tokens, random set of strings on every form on the website. These are validated to see if they come from the original website.
These are also unique to sessions and should have enough entropy.
* Many frameworks have CSRF tokens built-in.
* Setting the SameSite flag on a Set-Cookie header to Strict or Lax
    * Strict disables cross-site requests.
    * Lax only allows browsers to send cookies for top-level navigation.
* Chrome by default sets it to Lax. Attacks won't be able to do POST CSRF.
    * Firefox & Safari doesn't. Sometimes its set to None for third parties to send cross-site authenticated requests.
    * Attacks could try to use GET, so Lax could be circumvented.

### Hunting for CSRF

* Look for requests on forms that don't have CSRF protections and create a HTML page on a server you own to test cross site functionality. Then check if changes were made.
* Websites could be missing a CSRF token, but use refer-headers
    * If they are using refer-headers, try removing them with the <meta> tag. Or bypass the logic by setting paths/subdomain in the URL like a XSS.
* CSRF protections aren't always comprehensive. Exploit clickjacking to achieve the same result, change methods, and find validation issues like submitting requests with no CSRF tokens.
* Bypass Double-Submit CSRF tokens, which have cookies & paramters with the same values. Requests that don't have similar values for both will be invalid.
Token validity doesn't really matter as the server unlikely keeps track of the cookies validity.
 
