"""
5. Longest Palindromic Substring
Medium

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i, v in enumerate(s):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, h, t):
        while h >= 0 and t < len(s) and s[h] == s[t]:
            h -= 1
            t += 1
        return s[h + 1:t]


# print('b', left_idx, right_idx)\                    print('b', left_idx, right_idx)
s = Solution()
# test = s.longestPalindrome("cccc")
test = s.longestPalindrome("aalasdknflkddddsfajnkaasdasddddddddda")
print(test)