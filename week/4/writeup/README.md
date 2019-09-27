# Writeup 2 - Pentesting

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*

Eric's server runs the linux command `ping -c 2 {inserted hostname}`. The function however, does not do input sanitization. By adding a `;` after our hostname input, we can then add any command line command that we wish. To get to this point, I started out trying some of the shellshock injections from the slides, but then realized that did not make sense for this context of system. Looking up common command injections, I tried inputting `wattsamp.net; echo "Hello"` and was happy to see `Hello` printed to my screen. After finding this, I then inputted commands like `; ls -a` and kept similar commands up until running `; cd home; cat flag.txt` and getting the flag `CMSC389R-{p1ng_as_a_$erv1c3}`.

For Eric, always, __always__ sanitise your user inputs. Never trust any input the user inputs into your program. Additionally, not having your filesystem open to the internet for anyone to connect to would be a solid idea, or at least protected via password or through port 22 over ssh.

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

The main problem with implementing a reverse shell utilizing this vulnerability is the fact that the connection resets after each command. This is fine if you are running commands in just the `/` directory, but as soon as you want to branch out you need to save your directory that the command has moved into. My solution was to append `; pwd` to the end of each command run, then use some string manipulation to save the working directory and remove the output from the data outputted to the user. The current directory would be pre-appended to each command in the form of `; cd {curr_pwd}`. From there, the rest of the implementation was fairly straightforward.

