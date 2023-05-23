#Import all needed modules
from Modules.Style import *

#The list of the new commands
newcommands = [
    "banner",
    "quit",
    "q",
    "exit"
]

#Define the banner of EnDa Console
banner = """
$$$$$$$$\           $$$$$$$\                   $$$$$$\                                          $$\           
$$  _____|          $$  __$$\                 $$  __$$\                                         $$ |          
$$ |      $$$$$$$\  $$ |  $$ | $$$$$$\        $$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\  $$ | $$$$$$\  
$$$$$\    $$  __$$\ $$ |  $$ | \____$$\       $$ |      $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ 
$$  __|   $$ |  $$ |$$ |  $$ | $$$$$$$ |      $$ |      $$ /  $$ |$$ |  $$ |\$$$$$$\  $$ /  $$ |$$ |$$$$$$$$ |
$$ |      $$ |  $$ |$$ |  $$ |$$  __$$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ | \____$$\ $$ |  $$ |$$ |$$   ____|
$$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$$ |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$$$$$$  |\$$$$$$  |$$ |\$$$$$$$\ 
\________|\__|  \__|\_______/  \_______|       \______/  \______/ \__|  \__|\_______/  \______/ \__| \_______|
"""

#Define an command executor function
def commandExecutor(command):
    os.system(command)

#Define a variety of commands depends on operator system
def varietyCommandExecutor(other,windows):
    command = other
    if os.name in ("dos","nt"):
        command = windows
    os.system(command)

#Define an clear terminal function
def clearConsole():
    varietyCommandExecutor("clear","cls")

#Define a change directory function
def change_directory(dir_path):
    if not os.path.exists(dir_path):
        enter()
        error(f"Directory path '{Fore.LIGHTYELLOW_EX + dir_path + Fore.LIGHTRED_EX}' does not exist.")
    elif not os.path.isdir(dir_path):
        enter()
        error(f"{dir_path} can not be accessed!")
    else:
        os.chdir(dir_path)

#Define a main command executor
def mainexecutor(commands):
    try:
        if str(commands).lower() in ("q","quit","exit"):
            enter()
            outro("Roger that, exiting the program...",times=1.5)
            exit()
        elif commands.startswith("cd "):
            try:
                change_directory(dir_path = commands.split(' ', 1)[1])
            except:
                result = eval(commands)
                if result is not None:
                    print(result)
        elif str(commands).lower() == "banner":
                print(banner_color(banner,random.randint(1,5)))
        else:
            os.system(commands)
    except:
        pass
