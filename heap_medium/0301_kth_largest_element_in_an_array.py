"""
215. Kth Largest Element in an Array
Medium

2692

203

Favorite

Share
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
import heapq

class Solution:
    def findKthLargest(self, nums, k) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]

nums = [3,2,3,1,2,4,5,5,6]
k = 4

s = Solution()
test = s.findKthLargest(nums, k)
print(test==4)

