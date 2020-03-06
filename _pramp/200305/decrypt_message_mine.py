"""
ganster

input => crime

1.
ord(c) => 99
ord(r) => 114
ord(i) => 105
ord(m) => 109
ord(e) => 101

2.
99 => 100

3.
100
114 => 214
105 => 319
109 => 428
101 => 529

4.
subtract 26 till it will be in the range of ASCII


ASCII => 97 - 122
"crime"


decryption

input = 'dnotq'


1. add 26 till it will be in range of (index+1)*100 <= if it is not

d => 100 => 100
n => 110 => 136 => 162 => 188 => 214
o => 111 => 137 => 163 => 189 => 215 => 241 => 267 => 293 => 319
t => 116 => 142 => .. => 428
q => 113 => .. => 529



2. from last to second
=> we will substract previous value then replace the index's value with it
=> then the first value(meaning last turn of the loop) just - 1


3. we will convert that value to the character

d = 100 - 1 => 99 = c


n => 110 - 100 => 10 + 26m => range of ASCII (97 lower bound - 122 upper bound): 97 - 10 = ceil(8 / 26) = 4
...=> 11 + 26*4 = 114

input "crime"
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

# enc[n] => index n's value of list of encryption
# origin[n] => index n's value of list of origin value

Formula: enc[n] = origin[n] + enc[n-1] - 26m

# We want to get each origin[n] so that we can get whole origin word.
# Now we want to find origin[n] step by step

# Simply change the upper "Formula" for origin[n] is
origin[n] = enc[n] - enc[n-1] + 26m
# And origin[n] must be in the range of ASCII because we know it is ASCII number

# Simply because we know origin[0] == enc[0] - 1
# We can start from it
"""

# Time O(N)  <= O(N+k) N is for one for loop, k is process of finding m, O(N+k) => O(N)
# Space O(N) <= making of origins
def decrypt(word):
    if not word:
      return word
    encAsciis = [ord(i) for i in word]
    origins = []
    for i, v in enumerate(encAsciis):
      if i != 0:
        pre = v - encAsciis[i-1]
        m = 0
        while not (97 <= pre + 26*m <= 122):
          m += 1
        origins.append(pre+26*m)
    origins.insert(0, encAsciis[0]-1)
    return "".join((chr(i) for i in origins))

input = "dnotq"
test = decrypt(input)
print(test == "crime")