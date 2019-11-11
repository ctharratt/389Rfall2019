#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))


timestamp, = struct.unpack("<l", data[8:12])
time_readble = datetime.fromtimestamp(timestamp)
author = struct.unpack("<8s", data[12:20])
sections = struct.unpack("<L", data[20:24])
sections = sections[0]

print("TIMESTAMP: %s" % time_readble)
print("AUTHOR: %s " % author)
print("SECTION COUNT: %d" % sections)
print("DATA LENGTH : %d" % len(data))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
offset = 24
section_count = 0

while (section_count < int(sections)):
    section_count += 1
    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    stype = int(stype)
    slen = int(slen)
    #offset += 8

    print("SECTION TYPE: %d" % stype)
    print("SECTION LENGTH: %d" % slen)
    
    
    #SECTION_ASCII
    if (stype == 1):
        ascii = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        ascii = ascii[0]
        print(ascii)
        
    #SECTION_UTF8
    if (stype == 2):
        utf = struct.unpack(("<%ds" % slen), data[offset + 8: (offset + 8 + slen)])
        utf = utf[0]
        utf = utf.decode('utf-8')
        print(utf)
        
    #SECTION_WORDS
    if (stype == 3):
        word_number = int(slen/4)
        unpack = "<" + ("%s" % 'L' * word_number)
        words = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        words = words[0]
        print(words)
    
    #SECTION_DWORDS
    if (stype == 4):
        word_number = int(slen/8)
        unpack = "<" + ("%s" % 'L' * word_number)
        words = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        words = words[0]
        print(words)
        
    #SECTION_DOUBLES
    if (stype == 5):
        word_number = int(slen/8)
        unpack = "<" + ("%s" % 'd' * word_number)
        words = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        words = words[0]
        print(words)
        
    #SECTION_COORD
    if (stype == 6):
        data_result = struct.unpack("<dd", data[offset + 8: (offset + 8 + slen)])
        x = data_result[0]
        y = data_result[1]
        print("Coordinates: (" + str(x) + ", " + str(y) + ")")
        
    #SECTION_REFERENCE 
    #if (stype == 7):
    # svalue?
       
    #SECTION_PNG
    if (stype == 8):
        unpack = "<" + ("%s" % 'B' * (slen))
        its_magic_you_know = [137, 80, 78, 71, 13, 10, 26, 10]
        #its_magic_you_know = 0x89504E470D0A1A0A
        png_out = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        f = open('the_png.png', 'wb')
        #f.write(str(its_magic_you_know))
        f.write (bytearray(its_magic_you_know))
        f.write(bytearray(png_out))
        print("Png created")
        
    #SECTION_GIF87
    if (stype == 9):
        unpack = "<" + ("%s" % 'B' * (slen))
        its_magic_you_know = [47, 49, 46, 38, 37, 61]
        gif_out = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        f = open('the_gif87.gif', 'wb')
        f.write(bytearray(its_magic_you_know))
        f.write(bytearray(gif_out))
        print("Gif87 created")
    
    #SECTION_GIF89
    if (stype == 10):
        unpack = "<" + ("%s" % 'B' * (slen))
        its_magic_you_know = [47, 49, 46, 38, 39, 61]
        gif_out = struct.unpack(unpack, data[offset + 8: (offset + 8 + slen)])
        f = open('the_gif89.gif', 'wb')
        f.write(bytearray(its_magic_you_know))
        f.write(bytearray(gif_out))
        print("Gif89 created")
  
    offset = offset + slen + 8








