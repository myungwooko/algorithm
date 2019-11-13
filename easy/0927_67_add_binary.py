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



- True and Flase => False
- True + False => True
- divmod(a, b) => a를 b로 나눈 => 결과: 몫, 나머지
"""
class Solution(object):
    def addBinary(self, a, b):
        if not a or not b:
            return a or b

        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        a = [int(v) for v in a]
        b = [int(v) for v in b]

        if len(a) != len(b):
            if len(a) < len(b):
                volume = len(b) - len(a)
                for i in range(0, volume):
                    a.append(0)
            else:
                volume = len(a) - len(b)
                for i in range(0, volume):
                    b.append(0)

        next = 0
        result = []
        for i, v in enumerate(a):
            sum = v + b[i] + next
            if sum == 2:
                result.append(0)
                next = 1
            elif sum == 3:
                result.append(1)
                next = 1
            else:
                print(result, i, sum)
                result.append(sum)
                next = 0

        if next == 1:
            result.append(1)

        result.reverse()
        result = [str(v) for v in result]

        return "".join(result)


"""
using True False as 0 or 1 with 'and', 'or', '+'
"""
# class Solution(object):
#     def addBinary(self, a, b):
#         res, carry = "", 0
#         idx_a, idx_b = len(a) - 1, len(b) - 1
#         while idx_a >= 0 or idx_b >= 0 or carry:
#             curval = (idx_a >=0 and a[idx_a] == '1') + (idx_b >= 0 and b[idx_b] == '1')
#             carry, curval = divmod(curval + carry, 2)
#             res = str(curval) + res
#             idx_a -= 1
#             idx_b -= 1
#         return res



"""
Using binary methods
"""
# class Solution(object):
#     def addBinary(self, a, b):
#         x= int(a,2)                                  #convert a into binary
#         y= int(b,2)                                 #convert b into binary
#         print(1, x, y)
#         z=bin(x+y)                                #adds both integer converted values  and converts in into binary
#         print(2, x+y, bin(x+y))
#         print(3, z[2::])
#         return z[2::]                             # python binary prints 100 binary value like 0b100 slicing first 2 values returns the output


s = Solution()
test1 = s.addBinary('11', '1')
print(test1)

s = Solution()
test2 = s.addBinary('1010', '1011')
print(test2)