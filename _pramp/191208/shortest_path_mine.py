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
            if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] and (
                    r1, c1) not in seen:
                helper(r1, c1, seen + [(r1, c1)], count + 1)

    helper(sr, sc, [(sr, sc)], 0)
    return res[0]


# BFS
# Time Complexity: O(m*n), not exponential not like recursive solution and it can minimize because it return right away when it meets the answer
# Space Complexity: O(m*n), for seen
def shortestCellPath(grid, sr, sc, tr, tc):
    queue = [(sr, sc, [], 0)]
    row_bound = len(grid) - 1
    col_bound = len(grid[0]) - 1
    while queue:
        curr_r, curr_c, seen, count = queue.pop(0)
        if curr_r == tr and curr_c == tc:
            return count
        candidates = [(curr_r + 1, curr_c), (curr_r - 1, curr_c),
                      (curr_r, curr_c + 1), (curr_r, curr_c - 1)]
        for r1, c1 in candidates:
            if 0 <= r1 <= row_bound and 0 <= c1 <= col_bound and (
                    r1, c1) not in seen and grid[r1][c1]:
                queue.append((r1, c1, seen + [(r1, c1)], count + 1))

    return -1


# Time complexity: O(m*n)
# Space complexity: O(m*n)
def shortestCellPath(grid, sr, sc, tr, tc):
    queue = [(sr, sc, [(sr, sc)], 0)]
    while queue:
        x, y, seen, count = queue.pop(0)
        if x == tr and y == tc:
            return count
        possible = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        for x1, y1 in possible:
            if 0 <= x1 < len(grid) and 0 <= y1 < len(
                    grid[0]) and (x1, y1) not in seen and grid[x1][y1]:
                queue.append((x1, y1, seen + [(x1, y1)], count + 1))
    return -1


grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test)
