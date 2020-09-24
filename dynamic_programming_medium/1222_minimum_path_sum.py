"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    # recursive
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # res에는 최솟값만 해당 을 넘는건 버린다.
        # 더해 나갈때도 그거랑 비교해서 넘으면 바로 멈춘다.
        if not grid or not grid[0]:
            return 0
        res = []
        c, r = len(grid[0]), len(grid),
        self.allPaths(0, 0, c, r, grid, 0, res)
        print(3, res)
        return min(res)

    def allPaths(self, x, y, c, r, grid, sum, res):
        if x > c - 1 or y > r - 1:
            return
        if x == c - 1 and y == r - 1:
            sum += grid[y][x]
            if not res or sum < res[0]:
                res.append(sum)
            return
        sum += grid[y][x]
        if res and sum >= res[0]:
            return
        if x < c - 1:
            self.allPaths(x + 1, y, c, r, grid, sum, res)
        if y < r - 1:
            self.allPaths(x, y + 1, c, r, grid, sum, res)
        return

    # dp O(mn)
    def minPathSum(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = grid[0][0]
        print(0, grid[0])
        print(0, grid[1])
        print(0, grid[2])
        print(1, dp[0])
        print(1, dp[1])
        print(1, dp[2])
        """
        # 첫 포인트에서 아래쪽으로는 다른데서 더할거 없이 그쪽으로 그냥 가는게 합으로 나아가는 거고 다른데 들리지 않고 가장 작은거니깐 grid의 해당 값들을 하나씩 더해 나가서 더해진 수를 dp에 셋팅해준다. 
        """
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        print(2, dp)
        """
        # 첫 포인트에서 오른쪽으로는 다른데서 더할거 없이 그쪽으로 그냥 가는게 합으로 나아가는 거고 다른데 들리지 않고 가장 작은거니깐 grid의 해당 값들을 하나씩 더해 나가서 더해진 수를 dp에 셋팅해준다. 
        """
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        print(3, dp)
        """
        # 그 자리에 올수 있는애들은 자신의 왼쪽과 위쪽 2개가 있는데 그중에서 작은게 와야 해당 자리가 최소값으로 채워지는 거고 최소값끼리 더하면 결국 최소값을 만들수 있게 된다.
        # 결국 해당 로직으로 dp를 쭉 만들어 나가서 마지막에 dp[-1][-1]을 리턴하면 된다. 
        """
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(4, dp[0])
        print(4, dp[1])
        print(4, dp[2])
        return dp[-1][-1]


input = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution()
test = s.minPathSum(input)
print('result is:', test)
