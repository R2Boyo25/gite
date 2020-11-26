import os

def cprint(text, color):
    c=str(color)

    if not c.isdigit():

        raise Exception("Argument 'color' must be a number")

    os.system(f"tput setaf {c}")

    print(text)

    os.system("tput sgr0")


def run(command, success="", error=""):

    if success == "":

        success = f"{command} was successfully run!"

    if error == "":

        error = f"{command} failed to run!"

    if not os.system(command):
        
        cprint(success, 2)

    else:

        cprint(error, 1)
