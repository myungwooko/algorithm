"""
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

- Use problems conditions!
- There are answers in the problem.

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        half = len(nums) / 2
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > half:
                return num

    def majorityElement2(self, nums):
        """
        *** It said

        You may assume that the array is non-empty and the majority element always exist in the array.
        """
        nums.sort()
        return nums[len(nums) // 2]


s = Solution()
test = s.majorityElement([1,2,2,2,2,2,1,3])
test1 = s.majorityElement([3,2,3])
print(test)
print(test1)