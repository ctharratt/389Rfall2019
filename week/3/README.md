# Operational Security and Social Engineering

## Assignment details

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

You have been hired by a penetration testing firm and have been asked to collect some specific information about the Wattsamp employee from HW2, Eric Norman. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

- What's his mother's maiden name?
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?

Write up a pretext that you would use to social engineer this information out of Eric Norman. What approach would you take and how would you present yourself to elicit this information under the radar? Use the slides and what we covered in lecture to come up with a plan to obtain this information.


Call Eric J. Norman from OSINT number.

Hi Eric, this is Mark from BP Oil and Energy.
We are doing a financial audit on our systems and some of our records are incomplete from when you were previously employed here, do you think you can help me fill in the details?
I really need to get this done soon or my boss will be on my back.
[Response]
Great! I just need to confirm your identity with the information that we have so we can get this taken care of, what city were you born in?
[City born in]
Perfect, thank you Eric. Our records got scrambled with what paychecks went to each employee's bank, do you know which bank received your paycheck during your employment at BP?
[Bank Details Get]
That's great, I know a few people that use that bank, I've been thinking of switching myself over from [Any bank except the one they say], do you still use that bank currently?
[Polite conversation]
Do you remember how often you were paid? Every two weeks or monthly?
[Doesn't matter what they answer]
Okay perfect! Also, if you are interested since you were a previous employee at BP, if you would be willing to take a quick 2 minute survey on your experience, you will be entered
to potentially get tickets to season passes to Texas Longhorn Football games. (taken from instagram).
[Hopefully he says yes]
Great! I will send you the link, but we have different link depending on what browser you use, which one are you using right now?
[Browser use get]
*Send generic old employee satisfaction survey.
Thank you for the help Eric!


From this conversation we know what bank Eric J. Norman uses, we can then craft a security alert email for his bank:

Subject: Suspicious Activity Detected on your [Bank Name] card.
Body: Mr. Norman,

    Our fraud department has detected and blocked the following charges on your card:
    
    SPRINGHILL SUITES (9/19/19).............. $111.87
    RESIDENCE INN BY MARIOT (9/19/19)....... $157.07
    COURTYARD BY MARIOT (9/19/20)............ $330.45
    COURTYARD BY MARIOT (9/19/20) ........... $948.64
    
    
    We have placed a temporary hold on your card due to the potential fraudulent activity.
    
    Please call {Bank Name} Fraud Department from 8:00 am - 5:00 pm M-F @ [My Phone]
    
    [Bank Name] {Bank Logo}


Wait for the call if call:

[Bank Name] Fraud Department, my name is Luke, how may I help you?

I am sorry that happened to you Sir, can I get your name and account number?

I just need to verify some information from you Sir. What is your mother's maiden name?
[Maiden Name Get]
Okay, and what was the name of your first pet?
[First Pet Name Get]

Go through conversation talking about the card, suspicious charges, and how to get them removed, etc...

This is similar to reports that we have been getting from other customers, typically it is due to an insecure pin number. What is your pin number for your card?
[Pin Number Get]
That number is actually a very common pin number, I would recommend changing that at your local bank when you can as a precaution. I have removed the charges from your card and have
removed the temporary hold on your card. Is there anything else I can help you with today?

Thank you, have a good rest of your day Sir.


### Part 2

Eric Norman has recently discovered that Watsam's web server has been broken into by the crafty CMSC389R ethical hackers. After reading your published report, he has reached out to you to seek guidance in how he can repair some of the vulnerabilities that you have discovered.
Choose 3 specific vulnerabilities from homework 2 that you have identified (ie. exposed ports, weak passwords, etc.) and write a brief summary of some suggestions you can provide Eric for the Wattsamp web server and admin server. Be as thorough as possible in your answer, use specific examples and citing online research into security techniques that could be applied to the servers (ie. firewall, IDS/IPS, password managers, etc.).


1337 Port Vulnerability
    Access to your server from outside is important, but you should not be using this type of connection. Consider migrating to SSH over port 22 instead. If you continue to use your 1337 port instead, make sure that a single IP cannot keep trying and retrying username and password combinations. Installing an Intrusion Prevention System in your network will catch these repetitive connections from the same host and block connections to the server from that IP.
    
Password Vulnerability
    One of the reasons your 1337 port was vulnerable above was because of simple password complexit. hello1 is not a strong password. Consider implementing greater password security requirements, I.E. at least 8 characters in length, containing at least one special character and one number. Better yet, invest in password phrases instead of passwords. "The_Blue_Fox_Runs_Red_Lights!" is a strong password that is easy to remember. Otherwise, consider getting a password manager like lastpass to generate strong passwords quickly.
    
NMap Scanning
    One of the ways we got the information to attack 1337 was through NMap. Again, consider getting an IPS for your network. and IPS will be able to detect a IP constantly sending SYN packets across all 65,536 ports. Upon seeing an IP constantly sending SYN packets, and the network sending SYNACK packets back, the IPS should block further packets from the IP. This will strengthen your network against hackers and could give you a potential heads up when attackers are probing your system.


### Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.

### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
