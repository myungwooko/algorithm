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


# the range of lowercase letters a-z in ASCII: 97-122
# Formula for second~last: word[n] = lev1[n] + lev2[n-1] - 26*m
# lev1[n] = word[n] - lev2[n-1] + 26*m
# lev2[n] = lev2[n-1] + lev1[n]

# Time O(n)  <= O(n+k) N is for one for loop, k is process of finding m
# Space complexity: O(n) <= O(3n)
def decrypt(word):
    if not word:
        return word

    lev3 = [ord(char) for char in word]
    lev2 = [lev3[0]]
    lev1 = [lev3[0] - 1]

    for n in range(1, len(lev3)):
        before_add_26m = lev3[n] - lev2[n - 1]
        m = 1
        while before_add_26m + 26 * m < 97:
            m += 1
        lev1_nth = before_add_26m + 26 * m
        lev1.append(lev1_nth)
        lev2_nth = lev2[n - 1] + lev1[n]
        lev2.append(lev2_nth)

    return "".join([chr(asc) for asc in lev1])


# lev3[i] = lev1[i] + lev2[i-1] - 26*m
# lev1[i] = lev3[i] - lev2[i-1] + 26*m -> 97 <= range <=122
# lev2[i] = lev1[i] + lev2[i-1]
# Time complexity: O(n)
# Space compexity: O(n)
def decrypt(encrypted):
    if not encrypted:
        return encrypted
    lev3 = [ord(c) for c in encrypted]
    lev2 = [lev3[0]]
    lev1 = [lev3[0] - 1]
    for i in range(1, len(lev3)):
        pre_part = lev3[i] - lev2[i - 1]
        n = 1
        while not (97 <= pre_part + 26 * n <= 122):
            n += 1
        lev1_val = pre_part + 26 * n
        lev2_val = lev1_val + lev2[i - 1]
        lev1.append(lev1_val)
        lev2.append(lev2_val)
    return "".join([chr(n) for n in lev1])


word = "dnotq"
test = decrypt(word)
print(test == "crime")
