### Summary

Covers common algorithms and techniques that underly how modern day cryptography works.
Showcases how ransomware is implemented with publickey crpytography with a Python script
that encrypts one or multiple files. Excercises involve building a server that decrypts a symmetrical key
and returns it to the victim, and extending it so that it sends a copy of the encrypted key to the server.

### Encrypt.py

Book doesn't cover how to generate the key itself, so the solution I found that got this
script to work was to add some lines that used the rsa function from the cryptography library 
to generate a public key each time its executed, and therefore encrypts the .txt file with a different outcome each time.
