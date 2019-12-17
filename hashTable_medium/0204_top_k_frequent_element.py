"""
347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
import heapq
import unittest

# Complexity is O(Nlog(K)) O(N)
class Solution(object):
    def topKFrequent(self, nums, k):
        # 1.counter => freq mapping  2.items => make index order => keeping index order, make (freq, num) list
        d, h = [(freq, num) for num, freq in Counter(nums).items()], []
        print(1, Counter(nums), "<= "
                             "collections.Counter() Counter object create: freq first, between same freq index first <= ordering like this // "
                             "num: freq <= form like this *Counter object create")
        print(2, Counter(nums).items(), "<= if we call items() ordering from the counter object's to nums index order")
        for i in range(k):
            heapq.heappush(h, d[i])
        print(f"h => {h} <= heapq.heappush: it orders basically the one that smallest frequency will be first one")
        for i in range(k, len(d)):
            # iterate rest of d => if d[i] freq is bigger than smaller of h => swap those
            if d[i][0] > h[0][0]:
                #heapq.heappop(h): it pop first one
                heapq.heappop(h)
                # automatically sorted, in this case ordered by frequece
                heapq.heappush(h, d[i])
        return [heapq.heappop(h)[1] for _ in range(k)][::-1]


nums = [1, 7, 1, 2, 2, 4]
k = 2
s = Solution()
test = s.topKFrequent(nums, k)
print(test)
print(test==[2,1])




class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 7, 1, 1, 2, 2, 4]
        k = 2
        s = Solution()
        self.assertEqual(s.topKFrequent(nums, k), [1,2])

if __name__ == '__main__':
    unittest.main()



