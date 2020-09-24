"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        # if nums was given as empty array?
        # if all the numbers are negative => return the biggest one
        # it can be same integer inside?
        if not nums:
            return "You should put integer element(s) lsit as nums"

        if len(nums) == 1:
            return nums[0]

        idx = 0
        sum = 0
        sum_list = []
        while idx < len(nums):
            if sum + nums[idx] < sum:
                sum_list.append(sum + nums[idx])
                if sum + nums[idx] < 0:
                    sum = 0
                else:
                    sum += nums[idx]
            else:
                sum += nums[idx]
                sum_list.append(sum)

            idx += 1
        return max(sum_list)


"""
What a simple it is!!!
"""
# class Solution:
# # @param A, a list of integers
# # @return an integer
#     def maxSubArray(self, A):
#         if not A:
#             return 0
#
#         curSum = maxSum = A[0]
#         for num in A[1:]:
#             curSum = max(num, curSum + num)
#             maxSum = max(maxSum, curSum)
#
#         return maxSum

s = Solution()
#
test = s.maxSubArray(
    [8, -2, -4, -1, -8, 3, 8, 8, 3, 4, 2, -9, -1, -3, -6, 8, -3, 9])
print(test, '== 28 ?')

test2 = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(test2, '== 6 ?')

test3 = s.maxSubArray([-2, 1])
print(test3, '== 1 ?')

test4 = s.maxSubArray([-2, -1])
print(test4, '== -1 ?')
