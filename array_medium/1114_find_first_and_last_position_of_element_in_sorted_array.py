"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

if there is one target in the nums => [the index, the index]
if there is not target in the nums => [-1, -1]
if there is many target in the nums => [the smallest index, the biggest index]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        lo, hi = 0, len(nums) - 1
        the_idx = -1
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                the_idx = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        the_idx
        l, r = the_idx
        while (nums[l] == target and l >= 0) or (nums[r] == target and r < len(nums)):
            if nums[l] == target:
                l -= 1
            if nums[r] == target:
                r += 1
        l += 1
        r -= 1
        return [l, r]


s = Solution()
nums, target = [5,7,7,8,8,10], 8
test = s.searchRange(nums, target)
print(test)