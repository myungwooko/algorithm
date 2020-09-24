"""
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, v in enumerate(nums[:-3]):
            sec_i = i + 1
            while sec_i < len(nums) - 2:
                l = sec_i + 1
                r = len(nums) - 1

                while l < r:
                    s = nums[i] + nums[sec_i] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        if [nums[i], nums[sec_i], nums[l], nums[r]] not in res:
                            res.append(
                                [nums[i], nums[sec_i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                sec_i += 1
        return res


s = Solution()
nums = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
target = 0
test = s.fourSum(nums, target)
print(test)
