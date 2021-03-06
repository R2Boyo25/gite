import os, subprocess, runner, sys

"""

A simple program to make using git quicker
Fun Fact: I used this to upload itself to GitHub

"""


if len(sys.argv) == 1:

    print("You must choose a command!")

    quit()

com = sys.argv[1]

if com == "upload":

    os.system("git add .")

    message = ' '.join(sys.argv[2:]).replace('\"', '').replace("'", "")

    os.system(f"git commit -m \"{message}\"")

    os.system("git push -u origin master")

elif com == "init":

    os.system("git init")

    if len(sys.argv) == 3:

        url = sys.argv[2]

    else:

        url = input("Repo url: ")

    os.system(f"git remote add origin {url}")

elif com == "update":

    os.system("git pull")

elif com == "resume":

    if len(sys.argv) == 3:

        url = sys.argv[2]

    else:

        url = input("Repo url: ")

    os.system("git init")

    os.system(f"git remote add origin {url}")

    os.system(f"git pull {url}")

elif com == "status" or com == "modifications" or com == "changes":

    os.system("git status")

elif com == "log" or com == "history":

    os.system("git log")

elif com == "help":

    with open("/"+"/".join(__file__.split("/")[:-1])+"/"+"gitehelp.txt", "r") as file:

        print(file.read())

else:

    print("Command not found, sending to git.")

    os.system(f'git {" ".join(sys.argv[1:])}')
