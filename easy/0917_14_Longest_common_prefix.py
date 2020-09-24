"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs):
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret


s = Solution()

a = ["flower", "flow", "flight"]
# output: "fl"
b = ["dog", "racecar", "car"]
# output: ""

sol_a = s.longestCommonPrefix(a)
sol_b = s.longestCommonPrefix(b)

print(sol_a)
print(sol_b)
"""
line 3
=> zip(strs)  => allstring
=> zip(*strs) => string one by one
for i, letter_group in enumerate(zip(strs)):
    print(i, letter_group)

0 ('flower',)
1 ('flow',)
2 ('flight',)


for i, letter_group in enumerate(zip(*strs)):
    print(i, letter_group)

0 ('f', 'f', 'f')
1 ('l', 'l', 'l')
2 ('o', 'o', 'i')



line 6
=> set(('f', 'f', 'f')) => {'f'}
"""
