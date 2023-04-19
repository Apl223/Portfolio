### Bash principles

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
    * ">>" : Appends output to the end
    * "<" : Reads from file and uses it as input.
        * nmap $1 > $1_recon/nmap
    * " | " : Uses output of one program as input for another.
* Saves the output of a command in a variable:
   * VAR = $(command)

### Regex

* Describes search patterns.
* Consists of constants (strings) and operators (symbols that operate over strings)
* Characters:
    * \d matches digits
    * \w matches characters
    * \s matches whitespace, \S for non-whitespace
    * . matches a single char
    * \ escapes a special char
    * ^ matches start of thge string or line
    * $ matches the end of a string or line.
* Operators:
    * star - matches the preceding char zero or more times
    * plus symbol - matches the preceding char one or more times
    * {1,3} - matches preceding char one to three times.
    * {1,} - matches preceding char one or more times.
    * [abc] - matches one of the chars
    * [a-z] - matches one of the chars in the range.
    * (a|b|c) - matches either one.
    
Example: grep -E "^\S+\s+\S+\s+\S+

* -E denotes that regex will be used.
* We will be filtering a nmap output with this pattern, line by line.
* According to the regex, will be looking for lines that have 3 words (Denoted by S+, non-whitespace string with one or more characters) 
and 2 spaces (Denoted by s+, one or more spaces of whitespace). 
