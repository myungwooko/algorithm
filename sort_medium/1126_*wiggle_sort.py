"""
324. Wiggle Sort II
Medium

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(1, nums)
        for i in range(len(nums) // 2, 0, -1):
            #insert big ones to between small ones
            nums.insert(i, nums.pop())
        print(2, nums)
        if len(nums) > 0 and len(nums) % 2 == 0:
            print(3, nums)
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1]:
                    # below for loop will do
                    # if same numbers are attached, it will send the part that start from latter of them to last of the list.
                    # => that made attached numbers be separated and wiggle pairs will be sustained in their position.
                    # simply [1,3,2,2,4] => [2,4,1,3,2]
                    # and it will be excuted in case of nums length is even, and it will happen once.
                    # 길이가 짝수이고 중복이 존재하는 경우 붙을수 있는 가능성이 존재하는 것 같다.
                    for i in range(i, len(nums)):
                        nums.insert(0, nums.pop())
                    break
        return nums


nums = [1, 5, 1, 1, 6, 4]
nums1 = [1, 3, 2, 2, 3, 1]
nums2 = [1, 1, 2, 1, 2, 2]
nums3 = [1, 4, 4, 4, 4, 5, 1, 6]
nums4 = [1, 5, 1]
s = Solution()
test = s.wiggleSort(nums)
print(test)
