"""
698. Partition to K Equal Sum Subsets
Medium

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

- 그러니까 첫번째에서 쭉 잘들어가서 만족시켜서 True여야 True가 되는가보다.
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, m = divmod(sum(nums), k)
        if m: return False
        dp, n = [0] * k, len(nums)
        nums.sort(reverse=True)
        print(1, nums)

        def dfs(i):
            if i == n:
                # 마지막까지 다 체크했으면 이제 합이 다 똑같은지만 체크하면 되니까
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                print('nums', nums)
                print(2, dp)
                if dp[j] <= target and dfs(i + 1):
                    return True
                dp[j] -= nums[i]
                print(3, dp)
                if not dp[j]: break
            return False

        return nums[0] <= target and dfs(0)

nums = [4,3,2,3,5,2,1]
k = 4
s = Solution()
test = s.canPartitionKSubsets(nums, k)
print(test)
