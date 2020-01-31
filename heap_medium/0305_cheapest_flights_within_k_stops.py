"""
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
import collections
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        # K+1 ? => n 스탑의 비행 횟수는 결국 n + 1
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            # 한번 더 가는 것이 유효할수 있으려면 k가 1 보다 커야한다. 그래야 한번 가보는걸 해볼수 있는 조건인것. 0이면 이미 유효한 stop수를 다 쓴것으로 가보는 것이 무의미.
            if k > 0:
                for j in f[i]:
                    print(j)
                    # price 적은 것 순으로 일단 넣고 있다.
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1



s = Solution()
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

test = s.findCheapestPrice(n, edges, src, dst, k)
print(test)



"""
discuss

#1
Idea
It happen to be the same idea of Dijkstra's algorithm, but we need to keep the path.

More
More helpful and detailed explanation here:
https://en.wikipedia.org/wiki/Dijkstra's_algorithm

def findCheapestPrice(self, n, flights, src, dst, k):
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p
    heap = [(0, src, k + 1)]
    while heap:
        p, i, k = heapq.heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1))
    return -1
        
        
#2        
Note: The code has been updated at 2018-2-18 17:33:41 (MST) to fix a bug pointed by @chang17 and @jray319. Thanks!
Their test case should be added in. The testcases for the contest did not cover those.
The fix makes the solution not really a Dijkstra that it is losing some property that Dijkstra has to use a priority queue. Instead, it falls into a BFS like solution.
But since I effectively adapt it from Dijkstra, I decide to remain the original code in the bottom for anyone who is interested in the changes.

This is basically an implementation for the Dijkstra algorithm based on the description in the book "Cracking the coding _interview", page 634. Its description is really clear.
The only thing that is "adapted" is highlighted in the code # this two lines are important below.

Using vanila Dijkstra can help us figure out the shortest weighted path from the src to dst.
But then we lose the information of those paths that can reach dst with less stop.
So I record the information into the results list. Once it somehow reaches the dst from a path, we record it.

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        remain, ret, stop = [], float('inf'), 0
        weights = [sys.maxint for i in range(n)]
        graph = [{} for i in range(n)]
        for s,d,w in flights:
            graph[s][d]=w

        heapq.heappush(remain, (0, src))
        weights[src] = 0
        while remain and stop <= K:
            tmp, remain = remain, []
            while tmp:
                weight, node = heapq.heappop(tmp)
                for tonode, toweight in graph[node].items():
                    if weights[tonode] > weight + toweight:
                        weights[tonode] = weight + toweight
                        heapq.heappush(remain, (weights[tonode], tonode))    
                    # this two lines are important
                    if tonode == dst and weights[tonode]<ret:
                        ret = weights[tonode]
            stop+=1
        return ret if ret < float('inf') else -1
"""