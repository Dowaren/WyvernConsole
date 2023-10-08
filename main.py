import sqlite3

import wyvern
import wyvern as  w
import os
import getpass
import webbrowser
w.wyvern()
import socket
print("""

type help for command list

""")

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def main():
    while True:
        username = getpass.getuser()
        command = input(username + ": ")

        if command[0:4] == "help":
            print(f"""______________________________________________________________________
Hi thanks for using Wyvern! 
                    
list of commands:
                    
help - Displays a list of all commands and their description.

cls - clear the console

cmd (command)-  (windows/linux/MacOS console command)

web (url) - open link.

git (https://github.com/(user)/(repo name)) - download git repo

ip  - shows your ip

sql read (some/path/database.db) -  read database and save in database.txt.)

pip (path) - execute a pip command  (need python)

python (path) - execute a python file
______________________________________________________________________
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

        elif command[0:2] == "ip":

            print("""Wyvern: Your IP - """ + get_local_ip())


        elif command[0:8] == "sql read":
            path = command[9:]


            if ".db" in path:
                con = sqlite3.connect(path)

                with con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM sqlite_master WHERE type='table';")
                    rows = cur.fetchall()
                    rol = str(rows)
                    roll = (rol.split("'"))
                    cur.execute(f"SELECT * FROM {roll[5]}")
                    rolll = str(cur.fetchall())
                    my_file = open("database.txt", "w", encoding="utf-8")
                    my_file.write(rolll)
                    my_file.close()

                    print("saved .txt with database!")


        elif command[0:3] == "pip":

            os.system(command)

        elif command[0:6] == "python":
            os.system(command)

        else:
            print("Wywern: "
                  "Alas, the wyvern did not find such a command. Try help.")





main()
