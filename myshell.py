#!/usr/bin/python3
# 17308381 - Mark Micosa

import os, sys, readline, subprocess
import commands

# Commands called from file commands.py
builtins = {
    "cd": commands.change_directory,
    "dir": commands.directory,
    "echo": commands.echo,
    "clr": commands.clear,
    "environ": commands.environment,
    "pause": commands.pause,
    "help": commands.help,
}


def run(user_input):
    # If 'Enter' inputed, return prompt
    if user_input == "":
        return
    # Splitting terminal arguments
    tokens = user_input.split()
    # Position [0] will always be the command
    command = tokens[0]

    # Check if first argument is in builtins dictionary
    if command in builtins:
        # Run if present
        builtins[command](tokens)
    else:
        try:
            # Checks for background execution
            if tokens[-1] == "&":
                subprocess.Popen(tokens[0])
            else:
            # If not in builtins or background execute, run
                subprocess.run(tokens)
        except:
            # Not satisfy any conditions above, print exception
            print(command + ": command not found")


def main():
    # Check if file is given
    if len(sys.argv) > 1:
        # Open file
        with open(sys.argv[1]) as f:
            # Read in lines of file
            lines = f.readlines()
        # Loop through each line, run if executable
        for line in lines:
            run(line)
    else:
        # Prompt
        user_input = input(os.getcwd() + " ~> ")
        # Run if input given, unless "quit" is inputed
        while user_input != "quit":
            run(user_input)
            user_input = input(os.getcwd() + " ~> ")


if __name__ == "__main__":
    main()
