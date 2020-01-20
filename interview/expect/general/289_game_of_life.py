"""
289. Game of Life
Medium

1331

236

Add to List

Share
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other
cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        living cell, neighbors => n
        - 2 < n       => die
        - 2 or 3 == n => alive
        - n > 3       => die

        dead cell, neighbors =>n
        - 3 == n       => live
        """
        self.M = len(board)
        self.N = len(board[0])
        for i in range(self.M):
            for j in range(self.N):
                count = self.neigbor_process(board, i, j)
                if board[i][j]:
                    if count < 2 or 3 < count:
                        # 2 means it is alive now but will be dead next round
                        board[i][j] = 2
                else:
                    if count == 3:
                        # 3 means it is dead now but will be alive next round
                        board[i][j] = 3
        # 위와 같은 작업을 통해 전의 살아 있던 1(바꾸는데 영향을 주는)의 기록과 추후의 그것의 행보를 정해줄수 있다.
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1

    def neigbor_process(self, board, x, y):
        count = 0
        candidates = [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1),
                      (x - 1, y - 1)]
        for (x1, y1) in candidates:
            if 0 <= x1 < self.M and 0 <= y1 < self.N and (0 < board[x1][y1] <= 2):
                count += 1
        return count




