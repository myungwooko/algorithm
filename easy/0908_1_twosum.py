"""
1. Two Sum
Easy

11856

409

Favorite

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i


inst = Solution()
a = inst.twoSum([2, 7, 11, 15], 9)

print(a)

dick = {'a': 3, 'b': 4}

print('a' in dick)
print(4 in dick)
