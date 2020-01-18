"""
283. Move Zeroes
Easy

2783

98

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Accepted
593,511
Submissions
1,060,022
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums.append(0)
                count += 1
        idx = 0
        while count:
            if nums[idx] == 0:
                del nums[idx]
                count -= 1
            else:
                idx += 1
        return nums

    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            # zero는 그냥 지나가므로 그 자리가 zero에 기억되어있는게 되고
            # zero가 아닌게 나오면 그것과 바꿔주므로 zero를 뒤로 보내게 된다.
            # it passes zero, and that remains the zero's index as a record
            # and when it face not zero, swap it with zero => that makes zero goes to tail
        return nums

