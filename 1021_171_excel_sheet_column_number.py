"""
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string

        if not s:
            return 0

        alphabet = list(string.ascii_uppercase)
        result = 0
        idx = 0
        for i in reversed(range(len(s))):
            result += pow(26, i) * (alphabet.index(s[idx]) + 1)
            idx += 1

        return result


s = Solution()
test = s.titleToNumber("AZ")
print(test)
