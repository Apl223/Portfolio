### Single-Sign-On-Security Issues
#
* Allows users to access services from the same organization without having to login
  multiple times. Companies can centralize where users are logging in from
* Cookie sharing, SAML, and OAuth are the most common SSO methods. Each has strengths/weaknesses.
* Cookie sharing: Authentication is shared under locations under the same parent domain under
  the Domain flag. 
* If an attacker manages to steal a cookie for a user, they could use that
  account on the other sites.
* They could also use a **subdomain takeover** vulnerability, where an attacker registers
  for a hostname that a company previously had for a subdomain on a 3rd party site like AWS or GitHub pages.
  They would use a DNS CNAME record to point a subdomain to a third party site. Someone from that company would
  need to remove that CNAME after that site was unregistered, also called dangling CNAMEs. Malicious hosters
  could steal cookies with the CNAME still there.
* **SAML** - SSO is done through three parties: user, identity provider and service provider. The identity provider
  passes authentication and user info to the service provider. Attackers can intercept SAML responses and authenticate
  as someone else if the application doesn't protect integrity. If it either has encryption but no signature, or a weak
  signature, its vulnerable.
* You could achieve SQL injections with this.
* **OAuth** - User grants scope-specific access tokens to service providers by the identity provider. The service provider
  will request user info, which is the scope. The identity provider will create an access token to allow the service provider
  to access the info. Attackers can bypass this by stealing the access token via open redirect.
### Hunting for SSO, Subdomain takeover, and SAML vulnerabilities
#
* Build a list of subdomains. Look for third party hosted pages.
  AWS and GitHub are vulnerable to subdomain takeovers, but Squarespace and Google Cloud aren't
  Look for 404 responses and automate discovery.
* For OAuth, look for the value called oauth in requests & open redirects to smuggle tokens.
* For SAML, intercept traffic and look for keywords like saml or XML code. Then look for field names
  and tamper with them to see if it has a signature. If it does, try removing it.
