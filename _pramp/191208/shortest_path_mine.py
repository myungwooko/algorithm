"""
Shortest Cell Path
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc.
Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1.
Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer
"""


# DFS
# Time Complexity: O(m*n), but exponentail
# Space Compleixty: O(n) for seen
def shortestCellPath(grid, sr, sc, tr, tc):
    m = len(grid)
    n = len(grid[0])
    res = [-1]

    def helper(r, c, seen, count):
        if r == tr and c == tc:
            if res[0] == -1 or res[0] > count:
                res[0] = count
            return

        candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r1, c1 in candidates:
            if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] and (r1, c1) not in seen:
                helper(r1, c1, seen + [(r1, c1)], count + 1)

    helper(sr, sc, [(sr, sc)], 0)
    return res[0]


# BFS
# Time Complexity: O(m*n) <= but when it meets return right away and not exponential => way better
# Space Compexity: O(m*n) for seen
def shortestCellPath(grid, sr, sc, tr, tc):
    m, n = len(grid), len(grid[0])
    queue = [(sr, sc, [(sr, sc)], 0)]
    while queue:
        r, c, seen, count = queue.pop(0)
        if r == tr and c == tc:
            return count
        candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r1, c1 in candidates:
            if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] and (r1, c1) not in seen:
                queue.append((r1, c1, seen + [(r1, c1)], count + 1))

    return -1


grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test)