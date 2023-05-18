### Server-Side Request Forgery
#
* Lets an attacker send requests on behalf of a server to internal or external sources. Bypassing firewalls and assuming privilege.
* As an example, If you were to pass https://public.example.com/proxy?url=https://admin.example to a public facing proxy for an app, 
  it would allow for you to access an admin panel. The server should be trusted by the site that hosts that admin panel since its 
  an internal machine. This way, the vulnerable internet-facing server could allow for attackers to read files, make API calls, 
  and access internal services.
* SSRF's have a blind attack variety.  They are more valuable for network scanning when you can't get direct results.
* If profile images allow users to specify, you could get internal resource to display passwords. You could change a paramater 
  like user_id to user_id=1234&url=https://localhost/password.txt.
### Prevention
#
* Blocklist/Allowlist. **Blocklists are banned addresses while alllowlists allow only requests for specified URLs.**
  Blocklists are common.
* Maybe implemented with special headers or secret tokens in internal requests.
### Hunting for SSRF
#
* Source code review. Check if it validates user-provided URLs.
* If you can;t focus on features that fetch external resources, then look at Webhooks, file uploads,
  document and image processors, link expansions, thumbnails, proxies, and endpoints that processes user 
  provided URLs.
* Also check URLs embedded in files - XML or PDF files: hidden API points  that accept URLs and input in HTML tags.
* **Webhooks** - custom HTTP callback endpoints used as notification systems for events. It collects useful info regarding
  performance and keeps data in sync across multiple applications. You can find them in dev portals. Notifications are used to get
  their systems to start other processes.
* Pay close attention to erros such as:
    * "Error: cannot upload image: SSH-2.0-Open SSH..." means a SSRF exists, also shows a service banner. 
    * "Error: Requests to this address are not allowed" means that it has a protection mechanism like allowlists/blocklists. Could still be exploitable.
    * Response time is important too, quick responses could mean a port is closed while firewalls would cause a delay.
* You could also send requests by setting up a server of your own for blind attacks or setup a netcat listener.
* Bypass allow/block lists with encoding, IPv6, redirects, regex, and changing DNS records.
