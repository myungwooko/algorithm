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
#
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         self.grid = grid
#         self.seen = [len(grid[0]) * [True] for _ in range(len(grid))]
#         self.result = 0
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if self.grid[i][j] == '1' and self.seen[i][j] == True:
#                     self.result += 1
#                     self.dfs(i, j)
#         return self.result
#
#     def dfs(self, i, j):
#         self.seen[i][j] = False
#         count = 0
#         if i - 1 >= 0 and self.seen[i - 1][j] == True and self.grid[i - 1][j] == '1':
#             self.dfs(i - 1, j)
#             count += 1
#         if i + 1 < len(self.grid) and self.seen[i + 1][j] == True and self.grid[i + 1][j] == '1':
#             self.dfs(i + 1, j)
#             count += 1
#         if j - 1 >= 0 and self.seen[i][j - 1] == True and self.grid[i][j - 1] == '1':
#             self.dfs(i, j - 1)
#             count += 1
#         if j + 1 < len(self.grid[0]) and self.seen[i][j + 1] == True and self.grid[i][j + 1] == '1':
#             self.dfs(i, j + 1)
#             count += 1
#         if count == 0:
#             return


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.seen = set()
        self.result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == '1' and (i, j) not in self.seen:
                    self.result += 1
                    self.dfs(i, j)
        return self.result

    def dfs(self, i, j):
        self.seen.add((i, j))
        count = 0
        if i - 1 >= 0 and (i-1, j) not in self.seen and self.grid[i - 1][j] == '1':
            self.dfs(i - 1, j)
            count += 1
        if i + 1 < len(self.grid) and (i+1, j) not in self.seen and self.grid[i + 1][j] == '1':
            self.dfs(i + 1, j)
            count += 1
        if j - 1 >= 0 and (i, j-1) not in self.seen and self.grid[i][j - 1] == '1':
            self.dfs(i, j - 1)
            count += 1
        if j + 1 < len(self.grid[0]) and (i, j+1) not in self.seen and self.grid[i][j + 1] == '1':
            self.dfs(i, j + 1)
            count += 1
        if count == 0:
            return


s = Solution()
grid = [["1", "1", "1", "1", "0"]]
# grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
test = s.numIslands(grid)
print(test)

