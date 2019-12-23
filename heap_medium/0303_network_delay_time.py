"""
743. Network Delay Time
Medium

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.



Example 1:

{picture}

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
import collections
import heapq

#Heap => 다음 행선지를 계속 뽑아서 더해나가는 방식 = accumulating time, access next destination approach.
class Solution(object):
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (w + time, v))
        return max(t.values()) if len(t) == N else -1


s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
test = s.networkDelayTime(times, N, K)
print(test)