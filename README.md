# README

## 17308381 - Mark Micosa


*Basic shell project for CA216 - Operating Systems module. This is a user manual on operating and interacting with shell.*



##### LAUNCHING THE SHELL

Locate location of shell using “ls” and “cd” command in terminal
When in directory with shell file run “python3 myshell.py”
Shell can also run batch files if given one through command line using
“python3 myshell.py <batchfile>"




## COMMANDS

#### CHANGE DIRECTORY
*__Command: `cd <directory>` , `cd ..`__* <br>
Changes current directory if new <directory> supplied, else if will just return to the prompt.
If `cd ..` inputted it changes to previous directory if possible.

#### CLEAR SCREEN
*__Command: `clr`__*<br>
Clears all content of terminal except prompt if terminal is not already cleared.

#### DIRECTORY
*__Command: `dir <directory>`__*
Prints contents of given <directory>. If no new <directory> is provided, prints current working directory.
If invalid <directory> given, exception is caught.

#### ECHO
*__Command: `echo <args>`__*<br>
Displays args given into terminal followed by a new line character, stripping any trailing and leading whitespace.

#### ENVIRONMENT VARIABLES
*__Command: `environ`__*<br>
Lists all environ variables.

#### HELP
*__Command: `help`__*<br>
Displays interactive user manual in terminal.


#### PAUSE
*__Command: `pause`__*<br>
Shell prevented to take any input until `Enter` key inputted, shell becomes functional again.

#### QUIT
*__Command: `quit`__*<br>
Exits the shell.




## DESCRIPTIONS

#### ENVIRONMENT CONCEPTS
Environment variable pairs that can affect how a program runs. They are usually set at some point before a process is run. The process then reads and acts accordingly.

#### INPUT / OUTPUT REDIRECTION
Example: `echo help > text.txt`<br>
If the notation `<command>` > `<file>` is appended to any file that normally writes its output to standard output,
the output of the given `<command>` is then written to the given `<file>` instead of the terminal.
The notation `<command>` >> `<existing file>` appends the output to an existing file that you have made before executing this notation.

#### BACKGROUND EXECUTION
Example: `atom &`<br>
Running a program in the background of the shell and still having full functionality of the shell simultaneously.
Using the `&` symbol at the end signifies that you want this to run in the background.
