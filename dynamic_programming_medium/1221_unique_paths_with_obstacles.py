"""
63. Unique Paths II
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    # recursive
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        count = []
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        self.driver(0, 0, m, n, obstacleGrid, count)
        return sum(count)

    def driver(self, x, y, m, n, obstacleGrid, count):
        if x == m - 1 and y == n - 1 and obstacleGrid[y][x] == 0:
            count.append(1)
            return
        if x < m - 1 and not obstacleGrid[y][x + 1]:
            self.driver(x + 1, y, m, n, obstacleGrid, count)
        if y < n - 1 and not obstacleGrid[y + 1][x]:
            self.driver(x, y + 1, m, n, obstacleGrid, count)
        return

    # O(mn) space >>
    def uniquePathsWithObstacles1(self, obstacleGrid):
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * c for _ in range(r)]
        print(1, dp)
        dp[0][0] = 1 - obstacleGrid[0][0]
        print(2, dp)
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        print(3, dp)
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        print(4, dp)
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 -
                                                            obstacleGrid[i][j])
        return dp[-1][-1]


input = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
s = Solution()
test = s.uniquePathsWithObstacles(input)
print(test)
