"""
348. Design Tic-Tac-Toe
Medium

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""


class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.seen = set()
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if (row, col) in self.seen:
            return 0
        if player == 0:
            return ("Choose positive number as your player number")

        if 0 <= row < self.n and 0 <= col < self.n:
            self.board[row][col] = player
            self.seen.add((row, col))
            if self.finish(row, col):
                return player
        return 0

    def finish(self, row, col):
        if self.vertical(row, col) or self.horizontal(
                row, col) or (self.diagonal(row, col, "one") and self.diagonal(
                    row, col, "seven")) or (self.diagonal(row, col, "five") and
                                            self.diagonal(row, col, "eleven")):
            return True
        return False

    def vertical(self, row, col):
        val = self.board[row][col]
        candidates = [(row, col) for row in range(self.n)]
        for x, y in candidates:
            if val != self.board[x][y]:
                return False
        return True

    def horizontal(self, row, col):
        val = self.board[row][col]
        candidates = [(row, col) for col in range(self.n)]
        for x, y in candidates:
            if val != self.board[x][y]:
                return False
        return True

    def diagonal(self, row, col, direction):
        val = self.board[row][col]
        if direction == 'one':
            if row == 0 and col == self.n - 1:
                return True
            if row - 1 >= 0 and col + 1 < self.n and self.board[row -
                                                                1][col +
                                                                   1] == val:
                return self.diagonal(row - 1, col + 1, 'one')
            else:
                return False

        if direction == 'five':
            if row == self.n - 1 and col == self.n - 1:
                return True
            if row + 1 < self.n and col + 1 < self.n and self.board[row + 1][
                    col + 1] == val:
                return self.diagonal(row + 1, col + 1, 'five')
            else:
                return False

        if direction == 'seven':
            if row == self.n - 1 and col == 0:
                return True
            if row + 1 < self.n and col - 1 < self.n and self.board[row + 1][
                    col - 1] == val:
                return self.diagonal(row + 1, col - 1, 'seven')
            else:
                return False

        if direction == 'eleven':
            if row == 0 and col == 0:
                return True
            if row - 1 >= 0 and col - 1 >= 0 and self.board[row - 1][col -
                                                                     1] == val:
                return self.diagonal(row - 1, col - 1, 'eleven')
            else:
                return False


"""
diagonal은 전체에서의 n의 개수로 만들어지는 것을 말하는 것. 하긴 Bingo를 생각하면! ㅎㅎ <===============================================
"""


# simpler and better
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.seen = set()
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.board[row][col] == 0:
            self.board[row][col] = player

        for i in range(self.n):
            if self.board[i][col] != player:
                break
            if i == self.n - 1:
                return player

        for j in range(self.n):
            if self.board[row][j] != player:
                break
            if j == self.n - 1:
                return player

        for k in range(self.n):
            if self.board[k][k] != player:
                break
            if k == self.n - 1:
                return player

        row = 0
        for l in range(self.n - 1, -1, -1):
            if self.board[row][l] != player:
                break
            if l == 0:
                return player
            row += 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
