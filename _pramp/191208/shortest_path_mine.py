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



"""
dfs depth first search
"""
def shortestCellPath(grid, sr, sc, tr, tc):
    if not grid or not grid[0]:
        return -1

    results = []
    m = len(grid)
    n = len(grid[0])

    def helper(x, y, count, seen):
        if x == tr and y == tc:
            results.append(count)
        candidates = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        for x1, y1 in candidates:
            if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] and (x1, y1) not in seen:
                helper(x1, y1, count + 1, seen + [(x1, y1)])
                # <= personally seen has not to be referenced by all cases, each case has to keep doing this with their level's
                # seen
        return

    helper(sr, sc, 0, [])
    if not results:
        return -1
    return min(results)

grid = [
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test == 4)

grid = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test2 = shortestCellPath(grid, sr, sc, tr, tc)
print(test2 == -1)

grid = [
         [0,1,0],
         [1,0,0],
         [1,0,1]
        ]
sr, sc, tr, tc = 2, 0, 1, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test==1)



"""
bfs breadth first search
time O(R*C), space O(R*C)
bfs breadth first search
"""
def shortestCellPath(grid, sr, sc, tr, tc):
    if not grid or not grid[0]:
        return -1
    m = len(grid)
    n = len(grid[0])
    queue = [(sr, sc, 0, [])]
    while queue:
        x, y, depth, seen = queue.pop(0)
        if x == tr and y == tc:
            return depth
        candidates = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        for x1, y1 in candidates:
            if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] and (x1, y1) not in seen:
                queue.append((x1, y1, depth + 1, seen + [(x1, y1)]))
                # <= personally seen has not to be referenced by all cases, each case has to keep doing this with their level's
                # seen
    return -1


grid = [
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test == 4)

grid = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test2 = shortestCellPath(grid, sr, sc, tr, tc)
print(test2 == -1)

grid = [
         [0,1,0],
         [1,0,0],
         [1,0,1]
        ]
sr, sc, tr, tc = 2, 0, 1, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test==1)