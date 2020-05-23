"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

- 파이썬에 기존에 있는 함수명으로 변수명을 만들지 말것! => 참조하다가 에러나고 꼬이는 경우가 빈번하게 발생.
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 3:
            return sum(nums)

        first_sum = nums[0] + nums[1] + nums[2]

        if first_sum >= target:
            diff = first_sum - target
        else:
            diff = target - first_sum
        res_sum, diff = first_sum, abs(diff)

        for i, v in enumerate(nums[:-2]):
            l = i + 1
            while l < len(nums) - 1:
                r = l + 1
                while r < len(nums):
                    sum1 = nums[i] + nums[l] + nums[r]
                    print(sum1)
                    if sum1 == target:
                        return sum1
                    if sum1 >= target:
                        diff1 = sum1 - target
                    else:
                        diff1 = target - sum1

                    if abs(diff1) < diff:
                        res_sum = sum1
                        diff = diff1
                    r += 1
                l += 1
        return res_sum

    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # break early
                    return res
        return res



s = Solution()
arg1 = [1,2,4,8,16,32,64,128]
arg2 = 82
test = s.threeSumClosest(arg1, arg2)
print(1, test)