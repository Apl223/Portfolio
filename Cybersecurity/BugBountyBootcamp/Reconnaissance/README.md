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

