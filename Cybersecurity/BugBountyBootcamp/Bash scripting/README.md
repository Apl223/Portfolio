### Writing scripts for recon

* First line should interpertor we will be using with #!
    * !# /bin/bash
* $1 represents the first argument the user passed in. Continues to $2 and so on.
* When running programs inside the script, create a variable reference the location so you can reference it later when using it again.
* Change permissions with chmod so you can execute the script:
    * chmod +x recon.sh
    * +x gives **all** users permission to execute it.
    * chmod 700 recon.sh for owners only.
* Output to file operands.
    * Program > Filename: Replaces file content with program output. Creates the file if it doesnt exist.
    * >> : Appends output to the end
    * < : Reads from file and uses it as input
    * | : Uses output of one program as input for another.



