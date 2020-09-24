"""
136. Single Number
Easy

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

-what if some element appear 3 times?
- recuce => reduce(func, iterable) => 나아가면서 결과값축적 => 축적과 다음것을 하는 개념 => 축적값이 idx 0 이되고 그렇게 계속 앞의 두개를 함수돌려나가서 마지막에 하나의 값으로 만드는 것
- lambda 문법 => lambda 인자 : 리턴값 간단한함수 변수에 할당과 동시에 정의 => x = lambda x,y: x+y => x(5,10) =>15
"""
from functools import reduce


class Solution:
    def singleNumber(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


s = Solution()
ele1 = [2, 2, 1]
test1 = s.singleNumber2(ele1)

print(test1)
