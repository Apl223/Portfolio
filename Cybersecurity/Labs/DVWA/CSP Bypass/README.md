### Security level: LOW

* Policy on the source states that script sources allowed are from a bunch of wesbites, and self,
where you can upload your own xss and run on this page with the URL.

### Security level: MEDIUM

* scripts need to have the exact nonce value, and come from the same origin to execute.
Code can be executed from the form itself.
* <script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA="> alert(1) </script> 

### Security level: HIGH

* Intercept the packet and change the callback value. Since tags werent expecility allowed this time,
you cant insert tags.
* alert('1')
