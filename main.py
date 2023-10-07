import wyvern
import wyvern as  w
import os
import getpass

w.wyvern()



def main():
    while True:
        username = getpass.getuser()
        command = input(username + ": ")

        if command == "help":
            print("""______________________________________________________________________
Hi thanks for using Wyvern! 
                    
list of commands:
                    
help - Displays a list of all commands and their description.

cls - clear the console

cmd (command)-  (windows/linux/MacOS console command)

""")



        if command == "cls":
            os.system('cls')
            wyvern.wyvern()

        elif command[0:3] == "cmd":
            os.system(command[4:])
            print(f'''
Successfully executed command - "{command[4:]}"
            
            ''')


        else:
            print("Wywern: "
                  "Alas, the wyvern did not find such a command. Try help.")





main()
