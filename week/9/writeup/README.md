# Writeup 9 - Forensics II

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt


## Assignment details

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?

    `142.93.136.81`

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

    The attackers launched a port scanning attack after connecting to server's website on port 80. The attacker keeps sending Syn and waits until the server responds with Syn Ack, but never completes the handshake with an Ack. The attacking IP continues this for different ports. This is likely using `nmap` or another similar port scanning tool. 

3. What are the hackers' IP addresses, and where are they connecting from?

    `159.203.113.181`. Through a ip geo lookup, the IP is based in Clifton, New Jersey

4. What port are they using to steal files on the server?

    The attackers are using port 21 (ftp)

5. Which file did they steal? What kind of file is it? Do you recognize the file?

    The stole the file `find_me.jpeg`. It is a jpeg image file. 

6. Which file did the attackers leave behind on the server?

    The attackers left behind `greetz.fpff`.

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

    They should be able to implement protections against port scanning by blacklisting ip's that continue to not complete a tcp handshake across multiple ports. This should rapidly slow down their reconasance. Additionally, using a more secure service than FTP and a more secure password than `linkinpark` would be beneficial. 

### Part 2 (55 Pts)

1. When was `greetz.fpff` generated?
    
    The file was generated `2019-03-27 04:15:05`
    
2. Who authored `greetz.fpff`?

    The author was `fl1nch`
    
4. List each section, giving us the data in it *and* its type.

    SECTION TYPE: 1 => SECTION_ASCII
    Hey you, keep looking :)
    SECTION TYPE: 6 => SECTION_COORD
    Coordinates: (52.336035, 4.880673)
    SECTION TYPE: 8 => SECTION_PNG
    png file
    SECTION TYPE: 1 => SECTION_ASCII
    }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
    SECTION TYPE: 1 => SECTION_ASCII
    Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.

| __Flag__  | __How it was found__ |
| ------------- | ------------- |
|  CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}| Reversing string |
|  CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding} | Base64 decoding |
|  CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak} | Png file |
