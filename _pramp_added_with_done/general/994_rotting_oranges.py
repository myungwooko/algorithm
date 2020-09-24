"""
994. Rotting Oranges
Easy

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:
[photo]
a =
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""


class Solution:
    def orangesRotting(self, grid) -> int:
        time = 0
        fresh = 0
        while True:
            checker = [char for r in grid for char in r]
            if 1 not in set(checker):
                return time
            copied = [row[:] for row in grid]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        self.helper(grid, copied, i, j)
                    if i == len(grid) - 1 and j == len(grid[0]) - 1:
                        if copied == grid:
                            print(i, j, grid, copied)
                            grid[0][0] = 7
                            print(i, j, grid, copied)
                            return -1
                        time += 1
                        grid = [row[:] for row in copied]

    def helper(self, grid, copied, r, c):
        if r - 1 >= 0 and grid[r - 1][c] == 2:
            copied[r][c] = 2
            return
        if r + 1 < len(grid) and grid[r + 1][c] == 2:
            copied[r][c] = 2
            return
        if c - 1 >= 0 and grid[r][c - 1] == 2:
            copied[r][c] = 2
            return
        if c + 1 < len(grid[0]) and grid[r][c + 1] == 2:
            copied[r][c] = 2
            return
        return
