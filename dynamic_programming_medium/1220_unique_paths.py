"""
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution(object):
    # recursion
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        count = []
        self.recursion(0, 0, m, n, count)
        return sum(count)

    def recursion(self, x, y, m, n, count):
        if x == m - 1 and y == n - 1:
            count.append(1)
            return
        if x < m - 1:
            self.recursion(x + 1, y, m, n, count)
        if y < n - 1:
            self.recursion(x, y + 1, m, n, count)
        return count

    # dp O(mn) space
    # 1 세팅해놓고 => 1, 1 부터 시작한다. 해당 것의 값은 좌와 상 값의 합이다.
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


m, n = 4, 5
s = Solution()
test = s.uniquePaths(m, n)
print(test)

