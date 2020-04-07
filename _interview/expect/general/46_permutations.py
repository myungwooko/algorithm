"""
46. Permutations
Medium

3264

95

Add to List

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        res = []
        def helper(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for num in nums:
                if num not in path and path + [num] not in res:
                    helper(path + [num])
        for num in nums:
            helper([num])
        return res

