"""
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme.

For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message,
return the number of ways to decode it.

Examples:
input:  S = '1262'
output: 3

explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
"""
def decodeVariations(S):
    result = []
    charMap = {}
    for i in range(65, 91):
        charMap[str(i-64)] = chr(i)

    def helper(s, acc):
        if s == "" and acc:
            result.append(acc)
            return
        curr = ""
        for i, num in enumerate(s):
            curr += num
            if curr in charMap:
                if i < len(s):
                    helper(s[i+1:], acc+charMap[curr])
    helper(S, "")
    return len(result)


test = decodeVariations("1262")
print(test)


def decodeVariations(S):
    result = []
    asciiMap = {}
    for i in range(65, 91):
        asciiMap[i-64] = chr(i)

    print(1, asciiMap)

    def helper(s, path):
        if not s and path:
            result.append(path)
            return

        curr = ""
        for i, n in enumerate(s):
            curr += n
            if curr in asciiMap:
                helper(s[i+1:], path + asciiMap[curr])

    helper(S, "")
    print(1, result)
    return len(result)



test = decodeVariations("1262")
print(test)

