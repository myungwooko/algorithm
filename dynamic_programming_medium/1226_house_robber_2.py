"""
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def robDp(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                # 일단 본인 차례에서 자기 앞앞까지의 최대에 자기를 더할수는 있는 거고, 자기 바로전 dp에는 못더하는데
                # 그 두개를 비교하면 지금까지의 최대가 되는 것
                # 다음으로 넘어가도 똑같이 적용된다.
                # dp[1]을 할때는 앞에 더할 것 없는데 해당 식에서도 dp[-1]을 더하는게 되고 해당 값은 0이니깐
                # (dp기본세팅 & dp 기본lenght로 인해서)
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        # 맨앞과 맨뒤는 붙을 수 없으니깐
        return max(robDp(nums[1:]), robDp(nums[:-1]))

