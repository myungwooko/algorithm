"""
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        idx = 0
        while count >= 1:
            if nums[idx] > 1:
                nums.append(nums[idx])
                del nums[idx]
            elif nums[idx] < 1:
                nums.insert(0, nums[idx])
                del nums[idx + 1]
                idx += 1
            else:
                idx += 1
            count -= 1
        return nums

input = [2,0,2,1,1,0] # => [0,0,1,1,2,2]

s = Solution()
test = s.sortColors(input)
print(test)