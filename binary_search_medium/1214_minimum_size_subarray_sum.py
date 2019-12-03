"""
209. Minimum Size Subarray Sum
Medium

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which
the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        # we scan from left to right, "total" tracks the
        # sum of the subarray. If the sum is less than s,
        # right moves forward one step, else left moves forward
        # one step, left and right form a window.
        #
        # 1. 다 더하면서 딱 s 보다 커질때까지 가고
        # => 여기서 지나간 부분들은 r자체로서의 의미는 못가졌기때문에 r로서의 대상으로선 제외 되는 거고
        # 2. res = len(nums) + 1로하는 이유는 답이 없는 경우를 구분하기 위함. 최대"개수"가 len(nums) 니까
        # 3. 원래 n에서 m까지의 개수를 구하려면 1을 더해야함.(둘다 포함해서 구할때)
        # 4. 그렇게 조건을 만족시키는게 나오면 그 right 기준에서 최대한 l을 줄여나간것의 개수를 최소 res로 담아놓고
        # 5. 그 위치에서 또 남은 right을 하나씩 옮겨가면서 해당 r로부터 l과의 거리를 더 좁힐수 있는 세트가 있는지
        #    보며 마지막까지 순회
        #    그때까지 승리해서 남은 res를 return 한다.
        # => s를 넘는지를 매번 체크했으므로 거기서부터(멈췄던 r부터) 나아가며 세어도 모든 가능한 것을 세는 것이된다.
        l = sum = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= s:
                res = min(res, r-l+1)
                sum -= nums[l]
                l += 1
        return res if res <= len(nums) else 0