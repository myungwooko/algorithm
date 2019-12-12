"""
187. Repeated DNA Sequences
Medium

557

219

Favorite

Share
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
class Solution:
    def findRepeatedDnaSequences(self, s):
        hash = {}
        for i in range(len(s) - 9):
            k = s[i:i + 10]
            if not hash.get(k, None):
                hash[k] = 1
            else:
                hash[k] += 1
        res = []
        for k, v in hash.items():
            if v > 1:
                res.append(k)
        return res

seq = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = Solution()
test = s.findRepeatedDnaSequences(seq)
print(test == ["AAAAACCCCC", "CCCCCAAAAA"])