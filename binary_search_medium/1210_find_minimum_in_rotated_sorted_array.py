"""
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.recursion(nums)

    def recursion(self, nums):
        if len(nums) <= 2:
            return min(nums)
        midIdx = len(nums) // 2
        if nums[0] > nums[midIdx]:
            return self.recursion(nums[:midIdx + 1])
        elif nums[midIdx] > nums[-1]:
            return self.recursion(nums[midIdx:])
        else:
            return nums[0]

    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]