"""
18. 4Sum
Medium

1462

276

Add to List

Share
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

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

class Solution:
    # 2 for loops
    def fourSum(self, nums, target: int):
        nums.sort()
        pairs = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    four = nums[i] + nums[j] + nums[l] + nums[r]
                    if four < target:
                        l += 1
                    elif four > target:
                        r -= 1
                    else:
                        pairs.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return pairs


    # one for, many while loops
    def fourSum(self, nums, target: int):
        nums.sort()
        pairs = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            l, r = j + 1, len(nums)
            while l < r:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    four = nums[i] + nums[j] + nums[l] + nums[r]
                    if four < target:
                        l += 1
                    elif four > target:
                        r -= 1
                    else:
                        pairs.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                j += 1
        return pairs