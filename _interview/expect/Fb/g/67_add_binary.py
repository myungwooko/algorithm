"""
67. Add Binary
Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution(object):
    def addBinary(self, a, b):
        res, carry = "", 0
        idx_a, idx_b = len(a) - 1, len(b) - 1
        while idx_a >= 0 or idx_b >= 0 or carry:
            curval = (idx_a >= 0 and a[idx_a] == '1') + (idx_b >= 0 and b[idx_b] == '1')
            carry, curval = divmod(curval + carry, 2)
            res = str(curval) + res
            idx_a -= 1
            idx_b -= 1
        return res

    def addBinary(self, a, b):
        s, carry = "", 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            d1, d2 = int(a[i]) if i >= 0 else 0, int(b[j]) if j >= 0 else 0
            tmpSum = d1 + d2 + carry
            carry, rem = divmod(tmpSum, 2)
            s = str(rem) + s
            i, j = i - 1, j - 1
        return s


