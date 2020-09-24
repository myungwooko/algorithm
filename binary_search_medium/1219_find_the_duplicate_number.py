"""
287. Find the Duplicate Number
Medium

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one
duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        counter = {}
        for i in nums:
            if not counter.get(i, None):
                counter[i] = 1
            else:
                return i
        return

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        discuss: https://leetcode.com/problems/find-the-duplicate-number/discuss/72912/Python-solution-with-detailed-explanation
        - duplicate이 포함되면 "반"을 넘을 수 밖에 없다는 것을 이용하는 것 같다.
        - 개수로 가는거니깐 못넘었으면 더 큰게 더 많아서 그게 자연히 반을 넘은게 되는 거고.
        - 반은 결국 이쪽이 넘든 저쪽이 넘든 넘게 되는 거니깐.
        - 작은것의 총합 중간까지 못미쳤다는건 나머지 반이 안되는 쪽에 중복이 있다는 말이 된다.
        - l을 return? -> 외워버린다.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if sum([i <= m for i in nums]) > m:
                # 201개중 m인 index 100이 101개를 포함하고 있는거니까
                r = m
            else:
                l = m + 1
        return l


input = [1, 2, 3, 4, 4]
s = Solution()
test = s.findDuplicate(input)
print(test)
