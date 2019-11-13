"""
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


-  [1]: 왜내하면 i = 0일때, a[0]과 그전의 None을 비교하는게 아니라 엉뚱하게 a[0]과 a[-1]을 비교하게 되니까.
"""
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):  # [8]
            print(11, i)
            if nums[i] > 0: break  # [7]
            if i > 0 and nums[i] == nums[i - 1]: continue  # [1]

            l, r = i + 1, length - 1  # [2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if v > 0: break
            if i > 0 and v == nums[i - 1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + v + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[l], v, nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

s = Solution()
content = [-2,0,1,1,2]
test = s.threeSum(content)
print(test)

