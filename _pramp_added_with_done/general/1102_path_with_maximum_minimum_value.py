"""
1102. Path With Maximum Minimum Value
Medium

Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.
A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

Example 1:

Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:


Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9
"""
import heapq


class Solution:
    def maximumMinimumPath(self, A) -> int:
        res = A[0][0]
        m, n = len(A), len(A[0])
        minHeap = [(-A[0][0], 0, 0)]
        visited = set()
        while minHeap:
            # 결국 제일 큰거인 애들을 먼저 순으로 확인하면서
            # 제일 큰거 인애들을 계속 뻈으므로 그러면서 처음 만나는 마지막 까지 도달한 애면 가장 큰 애들애 의한 조합에 의한 거라는 걔념? 그럴 확률은 높아보이긴 한다. 아래에서도 말하듯 넣긴 다 넣는데.
            val, x, y = heapq.heappop(minHeap)
            # print(val,i,j,A[i][j])
            if res > -val:
                res = -val

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == m - 1 and y == n - 1:
                return res

            candidates = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            for x1, y1 in candidates:
                if 0 <= x1 < m and 0 <= y1 < n and (x1, y1) not in visited:
                    # 제일 큰 거를 맨 앞으로 오게 하는 heappush
                    # 넣긴 다 넣는다. 조건에 걸리지만 않으면
                    heapq.heappush(minHeap, (-A[x1][y1], x1, y1))
        return


s = Solution()
input = [[2, 0, 5, 2, 0], [2, 4, 4, 4, 3], [1, 5, 0, 0, 0], [5, 4, 4, 3, 1],
         [1, 3, 1, 5, 3]]
test = s.maximumMinimumPath(input)
print(2 == test)
