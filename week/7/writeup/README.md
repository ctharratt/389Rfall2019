# Writeup 7 - Forensics I

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it?
   `jpeg` file found by running `file image`.
   The rest of the following information was found by running `exiftool image`

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.

    GPS Location: 41 deg 53' 54.87" N 87 deg 37' 22.53" W
    Address: John Hancock Center, 875 N Michigan Ave, Chicago, IL 60611

3. When was this photo taken? Provide a timestamp in your answer.

    2018:08:22 11:33:24     August 22nd, 2018 at 11:33 AM

4. What kind of camera took this photo?

    The back camera of an iPhone 8.

5. How high up was this photo taken? Provide an answer in meters.

    Taken at an altitude of 539.5m above sea level.

6. Provide any found flags in this file in standard flag format.

| __Flag__  | __How it was found__ |
| ------------- | ------------- |
|  CMSC389R-{look_I_f0und_a_str1ng}| strings image > strings.txt && grep -i "CMSC" strings.txt |
|  CMSCR-{abr@cadabra} | Binwalking and extracting the hidden png file |
