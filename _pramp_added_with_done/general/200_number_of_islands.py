"""
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

lap time: 1:45:48
* took a too long time(almose 1) to conceive the problem.
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.seen = set()
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1" and (i, j) not in self.seen:
                    self.seen.add((i, j))
                    count += 1
                    self.dfs(i, j)

        return count

    def dfs(self, i, j):
        candidates = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
        for x1, y1 in candidates:
            if 0 <= x1 < self.m and 0 <= y1 < self.n and self.grid[x1][
                    y1] == "1" and (x1, y1) not in self.seen:
                self.seen.add((x1, y1))
                self.dfs(x1, y1)
        return


"""
[
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
"""

s = Solution()
grid = [["1", "1", "1", "1", "0"]]
# grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
test = s.numIslands(grid)
print(test)
