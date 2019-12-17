"""
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for i in s:
            if not hash.get(i, None):
                hash[i] = 1
            else:
                hash[i] += 1
        sortByFreq = sorted(hash.items(), key= lambda x: x[1], reverse=True)
        res = [i[0]*i[1] for i in sortByFreq]
        return "".join(res)

input = "tree"
s = Solution()
test = s.frequencySort(input)
print(test=="eetr")




























