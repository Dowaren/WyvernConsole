import wyvern
import wyvern as  w
import os
import getpass
import webbrowser
w.wyvern()



def main():
    while True:
        username = getpass.getuser()
        command = input(username + ": ")

        if command[0:4] == "help":
            print("""______________________________________________________________________
Hi thanks for using Wyvern! 
                    
list of commands:
                    
help - Displays a list of all commands and their description.

cls - clear the console

cmd (command)-  (windows/linux/MacOS console command)

web (url) - open link.

git (https://github.com/{user}/{repo name}) - download git repo
""")



        elif command == "cls":
            os.system('cls')
            wyvern.wyvern()

        elif command[0:3] == "cmd":

            print("""
            """)
            os.system(command[4:])

            print(f'''
Successfully executed command - "{command[4:]}"
            
            ''')


        elif command[0:3] == "web":
            webbrowser.open(command[4:], new=0, autoraise=True)


        elif command[0:3] == "git":

            webbrowser.open(command[4:] + "/archive/refs/heads/main.zip",  new=0, autoraise=True)

        else:
            print("Wywern: "
                  "Alas, the wyvern did not find such a command. Try help.")





main()
