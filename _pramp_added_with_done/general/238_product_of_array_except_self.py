"""
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

*********
Algorithm

1,2,3,4
=>   24,     12      8       6
=> 1 2x3x4, 1 3x4, 1x2 4, 1x2x3 1
   l   r    l  r    l  r    l   r

so we just need to make two lists
left =  [1,1,1x2,1x2x3]]
right = [1,4,4x3,4x3x2]
and then reverse right then multiply two values of each side
*

lap times 33:28:66
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        pre_left = nums[:len(nums) - 1]
        pre_right = nums[1:][::-1]
        n = len(nums) - 1

        left = []
        for i in range(n):
            if not left:
                left.append(pre_left[i])
            else:
                left.append(left[-1] * pre_left[i])
        left = [1] + left

        right = []
        for i in range(n):
            if not right:
                right.append(pre_right[i])
            else:
                right.append(right[-1] * pre_right[i])
        right = ([1] + right)[::-1]

        result = left
        for i in range(n + 1):
            result[i] = result[i] * right[i]

        return result


s = Solution()
input = [1, 2, 3, 4]
test = s.productExceptSelf(input)
print(test)
