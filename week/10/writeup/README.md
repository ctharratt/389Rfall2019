# Writeup 10 - Crypto I

Name: Chris Tharratt
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Chris Tharratt


## Assignment details

### Part 1 (45 Pts)

1) The ledger contains 16 bytes for the key hash, 16 bytes for the ciphertext hash, 16 bytes for the initiation vector, and then the lenght of the ciphertext for a total of 48 bytes + the size of the ciphertext.

2) The program uses md5 to hash the key, and MD5 for the key hash. The ciphertext is encrypted using AES128, then hashed with md5. MD5 hashes are pretty weak and are susceptible to collision attacks. They don't produce that long of a cryptographic hash, and is really quick to run the algorithm, so MD5 hashes can be brute forced or rainbowed quickly. AES128 isn't terrible, but there are better encryption algorithms out there.

3) The ledger has a size of 48 bytes + the cipher text. The given ledger has a total of 656 bytes so we know that the ciphertext is 608 bytes. Additionally, since you know the byte offsets, you can derive the key and cipher hashes, and the initiation vector.

4) The program uses AES128 to encrypt the data prior to writing it to the ledger. The encryption key is derived from using md5 to hash a password, taking the first two bytes, then hashing those two bytes again, with md5.

5) The ledger ensures integrity by checking the ciphertext hash with the stored hash and does the same with the key hash. However, since these are stored in the ledger, a person can modify the hashes with the new ciphertext and the program would not be able to detect the unauthorized change.

6) The application ensures authenticity by comparing the user entered password with the stored keyhash. This can be brute forced, especially since the key is only created from a 2 byte key.

7) The initialization vector is generated with `RAND_bytes(params.iv, 16)` and is then stored in the ledger. Since IVs just need to be random to be secure, it is fine to store them in plaintext in the ledger.


### Part 2 (45 Pts)

1) Code in crack.c. Basically loops through every potential 4 letter password and hashes it with md5 in attempt to find a hash that has the correct first 2 bytes. Do this by calling MD5 on the first 2 bytes like the ledger.c file does, and check that against the first 16 bytes of the ledger file. Return the password. Password: `ajTF`.

2) `CMSC389R-{k3y5p4c3_2_sm411}`

### Part 3 (10 Pts)

There are many problems with 'security' through obscurity. Obviously obscurity will potentially slow down an attacker, but people tend to be very persistent when it comes to getting into places they shouldn't. Eventually, either through luck, bad management, leaks, or persistence, the algorithm designed to be secure based on the fact that no one knows the algorithm will fall apart. Additionally, it places trust in a 3rd party. I would be hesitant to trust a developer that says "No guys, just trust me, this algorithm is secure, there are absolutely no back doors I added for myself, government agencies, or for people who pay me money, and I made sure I coded it well with 0 errors or bugs. 100% secure." Although this example is exaggerated, when an algorithm is obscured to provide security, no one knows how secure that algorithm is except the person who coded it, and they have complete control to modify it to suit their purposes, either intentionally malicious through backdoors, or unintentionally malicious through incompetence (cough wattsamp).
