"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

a = ['1', '2', '3']

seperator = ''

b = seperator.join(a)

print(-int(b))

print(1534236469 < pow(2, 31) - 1)


class Solution:
    def reverse(self, x: int) -> int:

        if not self.checker(x):
            return 0
        else:
            if x < 0:
                x = -x
                minus = True
            else:
                minus = False
            list_n = [x for x in str(x)]
            list_n.reverse()
            separator = ''
            ret = int(separator.join(list_n))
            if minus:
                ret = -ret
            return self.checker(ret)

    def checker(self, x):
        if x > (pow(2, 31) - 1) or x < -pow(2, 31):
            return 0
        else:
            return x
