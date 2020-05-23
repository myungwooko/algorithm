"""
79. Word Search
Medium

2837

145

Add to List

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    # DFS => Time Limit Exceeds
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False

        m = len(board)
        n = len(board[0])
        wordLen = len(word)
        results = []

        def helper(r, c, wordIdx, seen):
            if wordLen == wordIdx:
                results.append(True)
                return

            candidates = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
            for x1, y1 in candidates:
                if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] == word[wordIdx] and (x1, y1) not in seen:
                    helper(x1, y1, wordIdx + 1, seen + [(x1, y1)])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    helper(i, j, 1, [(i, j)])

        if True in results:
            return True

        return False


    #BFS Time limit exceeds
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False

        m = len(board)
        n = len(board[0])
        wordLen = len(word)
        queue = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    queue.append((i, j, 1, [(i, j)]))

        while queue:
            r, c, wordIdx, seen = queue.pop(0)
            if wordLen == wordIdx:
                return True
            candidates = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
            for x1, y1 in candidates:
                if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] == word[wordIdx] and (x1, y1) not in seen:
                    queue.append((x1, y1, wordIdx+1, seen + [(x1, y1)]))
        return False


    # It works
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False

        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, r, c, word):
        if len(word) == 0:
            return True

        if r < 0 or r >= self.m or c < 0 or c >= self.n or board[r][c] != word[0]:
            return False

        tmp = board[r][c]
        board[r][c] = "#"

        candidates = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
        for x1, y1 in candidates:
            if self.dfs(board, x1, y1, word[1:]):
                """
                why "return self.dfs(board, x1, y1, word[1:] instead of returning True" does not works?) => may be step by step and could meet False one first? => M
                """
                return True
        board[r][c] = tmp


board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
]
word = "ASAD"



s = Solution()
test = s.exist(board, word)
print(1, test)




