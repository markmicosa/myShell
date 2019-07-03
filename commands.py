# 17308381 - Mark Micosa

import os, subprocess

def change_directory(tokens):
    # If no new directory supplied, return
    if len(tokens) == 1:
        return
    else:
        try:
            # Change if valid directory given
            location = tokens[1]
            os.chdir(location)
            os.environ["PWD"]=os.getcwd()
        except:
            print('error: Directory not found')


def directory(tokens):
    try:
        # Print contents of new directory if given
        if len(tokens) == 1:
            for f in os.listdir(os.getcwd()):
                print(f)
        # Else print current directory
        else:
            for f in os.listdir(tokens[1]):
                print(f)
    except:
        # If invalid directory given
        print('error: Directory not found')

def echo(tokens):
    # Print every argument after poistion 1
    # Remove all leading and trailing whitespace
    print(' '.join(tokens[1:]))

def clear(tokens):
    # "\033c" ASCII code for "ESC" key, resets terminal
    # "end=""" to remove new line after clear
    print ("\033c", end="")

def environment(tokens):
    # Get key and values on os.environ dictionary
    for k, v in os.environ.items():
        print(k + " : " + v)

def pause(tokens):
    # Turn off echo
    os.system("stty -echo")
    # While "Enter" is not inputed, keep echo off
    while (tokens[0] != ''):
        tokens[0] = input()
        return os.system("stty echo")

def help(tokens):
    # Module subprocess runs "man" command on help file
    # Displays file in terminal
    subprocess.run(["man", "./help.groff"])
