"""
415. Add Strings
Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if (len(num1) != 1 and num1[0] == "0") or (len(num2) != 1
                                                   and num2[0] == "0"):
            return
        if not num1 or not num2:
            return num1 or num2
        if len(num1) > 5100 or len(num2) > 5100:
            return
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        li1 = list(num1)
        li2 = list(num2)
        container = 0
        res = []
        while li1 and li2:
            n1 = li1.pop()
            n2 = li2.pop()
            if n1 not in nums or n2 not in nums:
                return
            tmpSum = int(n1) + int(n2) + container
            if tmpSum > 9:
                container = 1
                tmpSum = int(str(tmpSum)[1])
            else:
                container = 0
            res.insert(0, tmpSum)
        head = li1 or li2
        if not head:
            if container:
                res.insert(0, container)
        else:
            for i in range(len(head) - 1, -1, -1):
                tmpSum = container + int(head[i])
                if tmpSum > 9:
                    container = 1
                    tmpSum = int(str(tmpSum)[1])
                    res.insert(0, tmpSum)
                else:
                    res.insert(0, tmpSum)
                    container = 0
            if container:
                res.insert(0, container)
        return "".join([str(i) for i in res])

    def addStrings(self, num1: str, num2: str) -> str:
        s = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            curSum = digit1 + digit2 + carry
            carry, rem = divmod(curSum, 10)
            s = str(rem) + s
            i, j = i - 1, j - 1
        return s
