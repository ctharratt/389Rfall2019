# Writeup 6 - Binaries I

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt

## Assignment Writeup

### Part 1 (50 pts)

`CMSC389R-{di5a55_0r_d13)`

### Part 2 (50 pts)

Starting out I opened up the crackme in binary ninja to see what was going on. After familiarizing myself with the code, I saw 4 methods in particular that were interesting. `update_flag`, `check1`, `check2`, `check3`. `update_flag` is called in each check function, so I assumed that checks1-3 were triggered in the main, and that a success on each check changed the final flag. I then decided to run crackme with `./crackme` and got `Did you even try disassembling?` as a result. So from here, the obvious interaction we have with the program is to pass arguments through a command line. `./crackme test` resulted in `Multi-word arguments can be quoted ;)`. Taking a closer look at `check1`, it calls strcmp and has the hardcoded string `"Oh God"`, a quick test of `./crackme "Oh God"` lets us progress on with a new hint: `I wish you cared more about the environment`. This plays into what check2 is checking, especially when the `getenv` function is called. Googling around, and with the string `FOOBAR` seen, this function is looking to see if an environmental variable named FOOBAR exists. The check checks this environment variable against a value, but sneakily does it in reverse order. So instead of checking for `seye ym `, it checks for ` my eyes`. Thus we now can run the command `FOOBAR=" my eyes" ./crackme "Oh God"` to get the first 2 checks done. The third check has something to do with files, as it opens a file named sesame (I enjoyed the pun). The file is read and then compared with a bunch of cases checking each hex value. Decoding, it looks for a string matching ` they burn`. Creating a file using `cat " they burn" > seasme`, I then tried to get the crackme to work without success until I eventually realized I spelled sesame as seasme. Fixing the file, we then get our flag: `CMSC389R-{di5a55_0r_d13)`.

The command `strings` looks for hardcoded text in the files, so all the method names and the hints are outputted, since they are specifically written in. The flag is a variable that is stored and then changed based on the outputs of each of the checks, since the flag is not hardcoded when stored into memory, `strings` will not be able to find it. Instead, we need to have each of the checks be true for the returns to work with the update_flag. The control flow is sequential with each of the checks:
check1: Checks the command line argument and does a strcmp.
check2: Checks for an environmental variable, and then looks at each letter in the string
check3: Checks to see if a file exists and contains the correct string.

All of the checks did some form of comparison against a correct string, just the locations of each of the strings were stored in a different way each time.

 











*Please use this space to detail your approach and solutions for part 2. Include
descriptions of checks implemented as well as your final input to produce flag.*
