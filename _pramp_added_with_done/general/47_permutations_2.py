"""
47. Permutations II
Medium

1642

56

Add to List

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        # sort() makes this fast version works
        nums.sort()
        res = []

        def helper(sub_nums, path):
            if len(path) == len(nums):
                res.append(path)

            for i in range(len(sub_nums)):
                # avoid positioning same value at same position
                # it makes working faster
                # and it is possible because we sorted our object
                if i > 0 and sub_nums[i] == sub_nums[i - 1]:
                    continue
                helper(sub_nums[:i] + sub_nums[i + 1:], path + [sub_nums[i]])

        helper(nums, [])
        return res


# Class methods
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         self.dfs(nums, [], res)
#         return res

#     def dfs(self, nums, path, res):
#         if not nums:
#             res.append(path)
#             return

#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
