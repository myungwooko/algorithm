"""
1. Two Sum

Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            key = target - nums[i]
            if not (key in hash):
                hash[key] = i
        return


s = Solution()
arr = [1, 2, 3, 7, 9, 11]
target = 11
test = s.twoSum(arr, target)
print(test == [1, 4])
