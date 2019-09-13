# Writeup 2 - OSINT

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*

Username: `ejnorman84`

1: `ejnorman84`'s real name is Eric J. Norman
2: `ejnorman84` works at Watts Amp Energy as a Powerplant Control Specialist. 
    URL: [http://wattsamp.net/](http://wattsamp.net/)
3: `ejnorman84` Personal Information:
| __Social Media__  | __Link__ |
| :-------------: | :-------------: |
| Reddit | [Reddit](https://www.reddit.com/user/ejnorman84/) |
| Instagram | [Instagram](https://www.instagram.com/ejnorman84/)|
| LinkedIn | [LinkedIn](https://www.linkedin.com/in/eric-norman-304550192/)|
| Twitter | [LinkedIn](https://twitter.com/ericnorman84)|
    
    Most of the above came from OsintFramework with various username checkers. The Twitter came from searching Eric J Norman on google with some search phrases. 
    
    Emails (From Twitter):
        1. ejnorman84@gmail.com
        2. ejnorman@protonmail.com
    
    Addtionally found a pastebin with some potential censored passwords to `ejnorman84`
    https://pastebin.com/4yJRgkFm
    
4:  IP Addresses:
    
    157.230.179.99 found with Reverse DNS lookup of http://wattsamp.net
    
    DNSDumpster and DNSTrails don't show many other IP's specific for this site, but do show the ips to other servers acting as the DNS:
    
    | ns-cloud-d4.googledomains.com | 216.239.38.109 |
    | ns-cloud-d3.googledomains.com	| 216.239.36.109 |
    | ns-cloud-d2.googledomains.com	| 216.239.34.109 | 
    | ns-cloud-d1.googledomains.com | 216.239.32.109 |
    

5: Using dirb, I found the following 'hidden' directories on the website
``` 
    ---- Scanning URL: http://wattsamp.net/ ----
    ==> DIRECTORY: http://wattsamp.net/assets/                                     
    + http://wattsamp.net/index.html (CODE:200|SIZE:6134)                          
    + http://wattsamp.net/LICENSE (CODE:200|SIZE:1093)                             
    + http://wattsamp.net/robots.txt (CODE:200|SIZE:63)                            
    + http://wattsamp.net/server-status (CODE:403|SIZE:277)                        
    ==> DIRECTORY: http://wattsamp.net/vendor/                                     
    ==> DIRECTORY: http://wattsamp.net/views/ 
```
    
    LICENSE gives us the standard MIT License, robots.txt gets us a flag, server-status requrires admin credentials, and the 3 directories gives us site information.
    Additionally, HTML comments on the admin page talks about a backend to the login page on the server, possibly a red herring. Have not been able to enumerate with that information yet. 
    
6: For this we use nmap and get the following output:
```
    Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-09 19:11 UTC
    Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
    Connect Scan Timing: About 2.30% done; ETC: 19:21 (0:09:11 remaining)
    Warning: 157.230.179.99 giving up on port because retransmission cap hit (6).
    Stats: 0:18:19 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
    Connect Scan Timing: About 56.65% done; ETC: 19:44 (0:14:01 remaining)
    Nmap scan report for wattsamp.net (157.230.179.99)
    Host is up (0.014s latency).
    Not shown: 65528 closed ports
    PORT      STATE    SERVICE      VERSION
    22/tcp    open     ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux;      protocol 2.0)
    | ssh-hostkey: 
    |   2048 13:b3:69:e2:06:86:7a:95:51:c2:91:ea:23:5e:69:84 (RSA)
    |   256 c9:2c:b8:4d:2b:cd:e1:1f:2b:74:16:15:c1:81:4e:ed (ECDSA)
    |_  256 de:9a:cb:7b:8a:f9:cc:3c:9f:7f:63:16:f8:71:1c:bf (ED25519)
    80/tcp    open     http         Apache httpd 2.4.29 ((Ubuntu))
    |_http-server-header: Apache/2.4.29 (Ubuntu)
    |_http-title: Wattsamp Energy
    135/tcp   filtered msrpc
    139/tcp   filtered netbios-ssn
    445/tcp   filtered microsoft-ds
    1337/tcp  open     waste?
    | fingerprint-strings: 
    |   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, LANDesk-RC, LDAPBindReq, NCP,   NULL, NotesRPC, RPCCheck, SMBProgNeg, TerminalServer, WMSRequest, X11Probe: 
    |     CAPTCHA ~~~
    |   FourOhFourRequest, GetRequest, HTTPOptions, RTSPRequest: 
    |     CAPTCHA ~~~
    |     Username: Password:
    |   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, SSLSessionReq, TLSSessionReq: 
    |     CAPTCHA ~~~
    |     Fail
    |   SIPOptions: 
    |     CAPTCHA ~~~
    |     Username: Password: Fail
    |   TerminalServerCookie: 
    |     CAPTCHA ~~~
    |_    Username:
    11211/tcp filtered memcache
```
    
    From this we see an interesting port 1337 (leet) open, which is likely the port that we need in part 2.
    
7: What OS is being used
  
    Using the above results, nmap also gives us a OS guess of OS: Linux. If we run nmap 157.230.179.99 -O to do a more aggressive test we get the following results:
    
```
    Aggressive OS guesses: Cisco Unified Communications Manager VoIP adapter (88%),     Android 5.0.1 (88%), Android 7.1.2 (Linux 3.10) (88%), Linksys WRV200 wireless broadband router (88%), DD-WRT v23 (Linux 2.4.36) (88%), DD-WRT v24-sp2 (Linux 2.4.36) (88%), Vyatta router (Linux 2.6.26) (88%), Linux 2.6.18 (88%), Linux 2.6.22 (Kubuntu, x86) (88%), Linux 2.6.25 (openSUSE 11.0) (88%)
```
This output is not too useful, but does imply that server itself is running some form of Linux. Additional testing on the website shows that it is running an `Apache/2.4.29` with `Ubuntu`. This was found when running Nikto against the site, and is displayed when viewing a 404 page. A Shodan search will also display that information.  
    
  
8: Bonus flags:

    | __Flag__  | __How it was found__ |
    | ------------- | ------------- |
    |  *CMSC389R-{html_h@x0r_lulz} | HTML Inspection |
    |  *CMSC389R-{n0_indexing_pls} | robots.txt |
    |  *CMSC389R-{Do_you-N0T_See_this} | DNS dumpster info |
    |  *CMSC389R-{LOOKING_CLOSELY_PAYS} | Instagram Photo |

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

My bruteforce program started simple enough. Make a function to solve the captcha, write a loop to loop through a wordlist, and send/receive the data. However, I ran into some problems when the server went down or when EDUROAM kicked me off the wifi crashing my program :/

The wifi was better in Iribe, and seemed to be faster, however, occasionally the data getting the captcha code was incorrect and not getting the full captcha. I added some checks to reloop the current iteration of the wordlist if a malformed captcha was received, or if the captcha failed for whatever reason.

I tried to use the pastebin of password creds by using "ejnorman84:p********a" and creating a new wordlist based on rockyou.txt with 10 digit passwords starting with p and ending with a. After running this for a bit, I realized that this was probably not the way it was intended to be done and just started with the standard rockyou.txt and found the correct password `hello` after 15 minutes or so.

After gaining access to the server, I realized the shell it gave us was not that great, as it crashed when moving back up directories, i.e `cd ..`. Using grep -r -i CMSC389R returned the location of the flag: `CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}` in the home directory. Trying other greps for passwords, usernames, login, backend, admin, etc revealed nothing interesting.

