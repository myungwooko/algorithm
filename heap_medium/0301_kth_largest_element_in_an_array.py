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
    # heapify => O(N), heappop => O(logN), but we do it (k-1) time => O((k-1)*logN)
    # => so it's time complexity is  O((k-1)*logN)
    def findKthLargest(self, nums, k) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]



    # O(N) => Using partition
    """partition의 개념은 pivot을 잡아놓고 그 전까지의 넘버들을 smaller idx와 순회하는 idx를 가지고 작은것을 앞으로 큰것들은 그것들 보다 뒤쪽으로 모아놓은뒤, 마지막 smaller idx의 위치는 
       smaller한거 모아놓고 마지막에 +1한 것이기때문에 그것을 우리의 기준인 pivot과 바꿔주는 개념 그러면 (pivot보다 작은것/pivot/pivot보다 큰것이 된다) 정확한 order는 관계없고 우리는 몇번째로 작은것인 그 값만
       구하면 되기 이런식으로 진행하면 그 값에 접근할수 있다."""
    def partition(self, nums, lo, hi):
        si = lo
        pivot = nums[hi]
        for i in range(lo, hi):
            if nums[i] <= pivot:
                nums[si], nums[i] = nums[i], nums[si]
                si += 1
        nums[si], nums[hi] = nums[hi], nums[si]
        return si

    def findKthLargest(self, nums, k) -> int:
        # smallest 기준으로 idx
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1

        """while loop이 있어도 결국 한번의 for loop을 매번 횟수마다 반복해서 도는 것일 뿐이므로 O(N)인것엔 변합이 없다."""
        while lo <= hi:
            idx = self.partition(nums, lo, hi)
            if idx == k:
                return nums[idx]
            elif idx < k:
                lo += 1
            else:
                hi -= 1
        return -1




    # 같은 partitioning
    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums) + 1 - k)


    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


nums = [3,2,3,1,2,4,5,5,6]
k = 4

s = Solution()
test = s.findKthLargest(nums, k)
print(test==4)

