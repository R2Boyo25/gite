import os, subprocess, runner, sys

if len(sys.argv) == 1:

    print("You must choose a command!")

    quit()

com = sys.argv[1]

if com == "upload":

    os.system("git add .")

    message = ' '.join(sys.argv[2:]).replace('\"', '')

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

    os.system(f"git remote origin {url}")

    os.system(f"git pull {url}")
