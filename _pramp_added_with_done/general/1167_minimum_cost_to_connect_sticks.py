"""
1167. Minimum Cost to Connect Sticks
Medium

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.


Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30


Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
Accepted

"""
import heapq


class Solution:
    # 축적된 비용에다가 다시 두개의 합을 더하는 것이기 때문에 축적된 비용을 최소화 시켜나가면 축적해 나가야 가장 작은 수를 만들수 있다.
    def connectSticks(self, A) -> int:
        heapq.heapify(A)
        cost = 0
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            cost += (x + y)
            heapq.heappush(A, (x + y))
        return cost


s = Solution()
test = s.connectSticks([2, 4, 3])
print(test == 14)
