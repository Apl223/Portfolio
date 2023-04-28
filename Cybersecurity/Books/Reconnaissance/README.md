### Google Dorking

Arguements:
* site - limits search scope to URL
* inurl - searches for a page via a URL.
* intitle - searches for a string on a page's title
* link - searches for web pages that contain links to a specified URL.
* filetype - searches for pages with a specific file ext.
* wildcard - search for any character or series of characters.
* Quotes - "" forces an exact match
* or - denoted as |, used to search for one term or both.
    * "how to hack" site:(reddit.com | stackoverflow.com
* minus - excludes results.
    * "how to hack" -php

###  Useful Google searches

* site:*.example.com
* site:*.example.com inurl:app/kibana
    * kibana is a data visualization tool. Displays server logs, stats and debug messages.
* site: s3.amazonaws.com COMPANY_NAME
    * Searches for company resources host by third party
* site: example.com ext:php
    * You can also search cfm,asp,jsp, and pl.
    * **Possibly download them and run them through a static code analyzer to find vulnerabilities.**
* site:example.com ext:txt password
    * searches example.com for text files containing "password".
* Check out exploit-db.com/google-hacking-database/
    * Practioners share their queries that could be useful for discovery here.

### WHOIS & reverse WHOIS

* Companies & individuals must provide identifying info when registering for a domain name to a domain registrar.
* These arent always available due to a domain privacy service, so you'd only see info from a forwarding service.
* You could do a reverse WHOIS on emails or phone numbers to find domains registered.
    * Reverse IP lookup works too with nslookup
    * If you run whois on the domain, check the "NetRange" field that shows the range of IPs the org has.
* IP addresses with the same ASN code number means they belong to the same org.
    * ASN stands for Autonomous system number which belong to publicly routable networks.
    * whois -h whois.cymru.com 157.240.2.20
    * h declares whois server to query
    * command will respond with the ASN

### Certificate Parsing

* Host info can also be found from SSL certs by checking the Subject Alternative Name field.
* This allows owners to reuse the same cert.
* crt.sh, Censys, Cert Spotter

### Subdomain Enumeration
* Once you have discovered domains under individuals or orgs, discover what subdomains there are.
* Tools: Sublist3r, SubBrute, Amass, Gobuster
    * Sublist3r queries search engines & databases
    * SubBrute guesses possible names.
    * Amass uses different methods.
    * Commonspeak2 generates wordlists based on Internet data.
    * SecLists has extensive wordlists for use.
        * Creating a wordlist with unique values between two files:
        sort -u WORDLIST1 WORDLIST2
        
### Service Enumeration
 * Tools: nmap, Shodan and Masscan
 
### Directory Enumeration
 * Tools: Dirsearch or Gobuster.
 * These will construct URL requests with wordlists, and return a status code.
     * 200 - file exists
     * 404 - doesn't exist
     * 403 - Protected. Examine these files to see if you can circumvent it.
 * Use OWASP Zed Attack Proxy for web spidering or crawling. 
 
