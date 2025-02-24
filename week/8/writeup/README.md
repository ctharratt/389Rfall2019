# Writeup 8 - Binaries II

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The administrator password is generated by first seeding the rand function with the current time then running `password[i] = rand() % ('z'-' ') + ' ';` 16 times for each character. This implementation is weak since we have the code of the server and can theoretically generate the same admin password by running the program at the same time that our instance is created when connecting to the server. Additionally, the password is a fixed 16 characters and allows for unlimited guesses. We can do a bruteforce attack against this implementation. 

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

Line 69: `gets(buff);` uses gets on a fixed size buffer. Since gets can read in any amounts of data, the buffer of 32 bits can be overwritten and is a Buffer Overflow Vulnerability.

Line 47: `printf(output);` prints the output without forcing the output to be a string. Not as immediately as dangerous as using gets() (the compiler doesn't warn us) this code can be used to print data off the stack using %s, %d, etc... Since the user can control what the output is, this is dangerous and is a Format String Vulnerability. 

3. What is the flag?
`CMSC389R-{expl017-2-w1n}`

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

At first I thought it would be easiest to copy over the code that generates the admin password locally, then run that program as I connected to the server. I created generate_pass.c and copied over the code with a loop to create 5 passwords to compensate for latency. I then compiled it and ran the command `./a.out & nc ec2-18-222-89-163.us-east-2.compute.amazonaws.com 1337`. Trying multiple times and all the generated passwords I could not get the right password to work. I attempted to change the number of loops, changing around some of the code I deleted when trimming the server.c code, as well as creating a bash script to run them concurrently (which the & command should have done in my original command) but nothing seemed to be getting me the correct password. Stumped for a while, I took another look at the server.c code looking for what I was missing. Running the server.c through gdb and messing around a ton with printf in the ciphertext, I discovered that the password is stored 29 positions down the stack through some trial an error and gdb. We can format a string that when printed will print out the key. We can format 28 %d's followed by a %s to get the string. `%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%s` is the string. I first tried to use this but didn't get the expected output, then I realized I needed to rot13 it first. `%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%f`. This string did not work, and after looking again and facepalming at my error, I realized that since the string is greater than the buffer allocated, the program won't read it all into memory and into the output variable. Googling, I found that a more efficient way to print with long double, which uses 12 bytes and can be represented by `%Lf`. We can then change our string to be instead `%Lf%Lf%Lf%Lf%Lf%Lf%Lf%Lf%Lf%d%f`, then rot13 it into `%Ys%Ys%Ys%Ys%Ys%Ys%Ys%Ys%Ys%q%f`. Now we can finally get the admin password with the last string that is printed.

After getting the admin password, to progress we need to exploit the buffer overflow vulnerability on line 69. The buffer is 33 bytes, and commands need to be null terminated with Ctrl+@. The command we then run is `cat flag^@;;;;;;;;;;;;;;;;;;;;;;;;;cat flag` with ^@ being the null terminator of Ctrl+@. We get the flag `CMSC389R-{expl017-2-w1n}`. 
                                  
