#Import all needed modules
from Modules.Style import *
from Modules.CustomCommands import *

#Define a funny art
funnyart = """
 ______________ 
< EnDa Console by EnDaTeam >
 -------------- 
      \                    / \  //\
       \    |\___/|      /   \//  \\
            /0  0  \__  /    //  | \ \    
           /     /  \/_/    //   |  \  \  
           @_^_@'/   \/_   //    |   \   \ 
           //_^_/     \/_ //     |    \    \
        ( //) |        \///      |     \     \
      ( / /) _|_ /   )  //       |      \     _\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
 (( /// ))      `.   {
"""

#The EnDa Console's code
clearConsole()
if os.name in ("dos","nt"):
    os.system("title EnDa Console ^| EnDaTeam")
print(banner_color(banner,random.randint(1,5)))
enter()
print(Fore.CYAN + "[========================================== " + Fore.LIGHTRED_EX + "WELCOME TO ENDA CONSOLE" + Fore.CYAN + " ==========================================]" + Fore.RESET)
print(Fore.CYAN + "[================================ " + Fore.LIGHTYELLOW_EX + "Execute 'HELP' for help and 'EXIT' for exit" + Fore.CYAN + " ================================]" + Fore.RESET)
enter()
while True:
    try:
        enter()
        commands = input(Fore.MAGENTA + "[#] " + Fore.WHITE + "EnDaConsole" + Fore.YELLOW + f" ({os.getcwd()})" + Fore.RESET + " >> ")
    except KeyboardInterrupt:
        enter()
        enter()
        error("If you want to leave the console please type 'QUIT' (Q) or 'EXIT'!")
    else:
        try:
            mainexecutor(commands)
        except KeyboardInterrupt:
            enter()
            enter()
            error("If you want to leave the console please type 'QUIT' (Q) or 'EXIT'!")