"""
202. Happy Number
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

- dict looks working better than set.
- and "dict.get(a)" works better than "a in dict" for lookup.
- 처음의 n이 1이 아니면 바로 넣어도 되는 이유는 어차피 밑에서 계산하고 나가는 거면 넣는다해도 다음 while문 check 단계에서 바로 벗어나서 True로 가므로
-> 그렇지 못했으면 바로 중복되는 경우 False로 가는 대상이 되는게 맞으므로.
"""
class Solution(object):
    def isHappy(self, n):
        dict_past = {}
        while n != 1:
            a = dict_past.get(n, None)
            if a:
                return False
            dict_past[n] = 1
            n = sum([int(i)**2 for i in str(n)])
        return True

    def isHappy2(self, n):
        c_dup = set()
        while n != 1:
            if n in c_dup:
                return False
            c_dup.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return True

s = Solution()
test = s.isHappy(19)
print(1, test)