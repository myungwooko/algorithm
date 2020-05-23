"""
Decrypt Message
An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking,
has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense,
the agency learned that they indeed encrypt their messages, and studied their method of encryption.

Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one,
add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII.
Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that
consists of small latin letters only, and returns the decrypted word.

Explain your solution and analyze its time and space complexities.

Examples:

input:  word = "dnotq"
output: "crime"

input:  word = "flgxswdliefy"
output: "encyclopedia"
Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space.
Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.

Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa.
You may search the internet for the appropriate method.

Constraints:

[time limit] 5000ms

[input] string word

The ASCII value of every char is in the range of lowercase letters a-z.
[output] string
"""

"""
##Encryption

input => crime 

1. 
ord(c) => 99
ord(r) => 114
ord(i) => 105
ord(m) => 109
ord(e) => 101

2. 
99 + 1 => 100

3. 
100
114 => 214
105 => 319
109 => 428
101 => 529

4.
subtract 26 till it will be in the range of ASCII

------------------------------------------------------------------------------


ASCII => 97 - 122

# Get the ASCII number of a character
number = ord(char)

# Get the character given by an ASCII number
char = chr(number)


------------------------------------------------------------------------------
## Dcryption

step1: origin
step2: lev2
step3: enc

**Formula**
=> enc[i] = lev2[i-1] + origin[i] - 26*m
=> origin[i] = enc[i] - lev2[i-1] + 26*m(has to > 96)

# as you can see we need lev2[i-1] when we get origin[i] so we need to updated it before using it
# As next lev2[i-1]
=> lev2[i] = lev2[i-1] + origin[i]
"""
# lev3[n] = lev2[n-1] + lev1[n] - 26*n
# lev1[n] = lev3[n] - lev2[n-1] + 26*n *96 < lev1[n] < 123

# Time O(n)  <= O(n+k) N is for one for loop, k is process of finding m, O(n+k) => O(n)
# Space complexity: O(3n)
def decrypt(word):
    if not word:
        return word
    lev3 = [ord(c) for c in word]
    lev2 = [lev3[0]]
    lev1 = [lev3[0] - 1]

    for i in range(1, len(lev3)):
        seg = lev3[i] - lev2[i - 1]
        print(seg)
        count = 1
        n = 1
        while seg + 26 * n < 97:
            n += 1
        lev1.append(seg + 26 * n)

        add_lev2 = lev2[i - 1] + lev1[i]
        lev2.append(add_lev2)

    return "".join([chr(n) for n in lev1])