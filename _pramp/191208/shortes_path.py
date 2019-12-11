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

# 1인데는 다 가는데
# 어디에서고 지나온데는 어디에서고 안간다.
# 지금 이건 memory가 모두 참조의 영향을 받고 있다. => pramp에서 통과는 된다.
"""
This function passes pramp test cases. Considering the function's name, I think it is wrong though.
In this case, memory is referenced by each different cases.
let's assume

grid = [
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test == 6) => False

it should be 6 but this function returns 8
let's look at another function below.
"""
def shortestCellPath(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    res = []
    rows = len(grid) - 1
    columns = len(grid[0]) - 1
    if sr == tr and sc == tc:
        return -1

    def helper(cr, cc, length, memory):
        if cr == tr and cc == tc:
            if not res:
                res.append(length)
            else:
                if length < res[0]:
                    res[0] = length
            return
        if cc + 1 <= columns and grid[cr][cc + 1] and (cr, cc + 1) not in memory:
            # print(1, cr, cc, memory)
            memory.append((cr, cc))
            helper(cr, cc + 1, length + 1, memory)
        if cr + 1 <= rows and grid[cr + 1][cc] and (cr + 1, cc) not in memory:
            # print(2, cr, cc, memory)
            memory.append((cr, cc))
            helper(cr + 1, cc, length + 1, memory)
        if cc - 1 >= 0 and grid[cr][cc - 1] and (cr, cc - 1) not in memory:
            memory.append((cr, cc))
            helper(cr, cc - 1, length + 1, memory)
        if cr - 1 >= 0 and grid[cr - 1][cc] and (cr - 1, cc) not in memory:
            memory.append((cr, cc))
            helper(cr - 1, cc, length + 1, memory)

    helper(sr, sc, 0, [])
    if res:
        return res[0]
    return -1

grid = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath(grid, sr, sc, tr, tc)
print(test == 8)

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









# 1인데는 다 가는데
# 각 케이스별로 지나간데는 안가지만 recursion의 내부 영역에 포함되지 않는 새로운 영역의 것들은 다른 recursion 영역에서 간것과 상관없이 자신 영역 내에서 counting을 한다.
# 지금 이건 memory가 각각의 recursion 영역을 보존하며 counting하고 있다. => 개인적으로 함수의 이름대로라면 이게 맞다.
"""
Considering the function's name, I think this is right.
In this case, memory is not referenced by each different cases.
let's assume

grid = [
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath1(grid, sr, sc, tr, tc)
print(test == 6) => True

it return the shortestCellPath
"""
def shortestCellPath1(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    res = []
    rows = len(grid) - 1
    columns = len(grid[0]) - 1
    if sr == tr and sc == tc:
        return -1
    def helper(cr, cc, length, memory):
        if cr == tr and cc == tc:
            if not res:
                res.append(length)
            else:
                if length < res[0]:
                    res[0] = length
            return
        # if cc + 1 <= columns and grid[cr][cc + 1] and (cr, cc + 1) not in memory:
        #     memory1 = memory[:]
        #     memory1.append((cr, cc))
        #     helper(cr, cc + 1, length + 1, memory1)
        # if cr + 1 <= rows and grid[cr + 1][cc] and (cr + 1, cc) not in memory:
        #     memory2 = memory[:]
        #     memory2.append((cr, cc))
        #     helper(cr + 1, cc, length + 1, memory2)
        # if cc - 1 >= 0 and grid[cr][cc - 1] and (cr, cc - 1) not in memory:
        #     memory3 = memory[:]
        #     memory3.append((cr, cc))
        #     helper(cr, cc - 1, length + 1, memory3)
        # if cr - 1 >= 0 and grid[cr - 1][cc] and (cr - 1, cc) not in memory:
        #     memory4 = memory[:]
        #     memory4.append((cr, cc))
        #     helper(cr - 1, cc, length + 1, memory4)

        # this is better and simpler for reference than right before
        if cc + 1 <= columns and grid[cr][cc + 1] and (cr, cc + 1) not in memory:
            memory.append((cr, cc))
            helper(cr, cc + 1, length + 1, memory + [(cr, cc)])
        if cr + 1 <= rows and grid[cr + 1][cc] and (cr + 1, cc) not in memory:
            memory2 = memory[:]
            memory2.append((cr, cc))
            helper(cr + 1, cc, length + 1, memory + [(cr, cc)])
        if cc - 1 >= 0 and grid[cr][cc - 1] and (cr, cc - 1) not in memory:
            memory3 = memory[:]
            memory3.append((cr, cc))
            helper(cr, cc - 1, length + 1, memory + [(cr, cc)])
        if cr - 1 >= 0 and grid[cr - 1][cc] and (cr - 1, cc) not in memory:
            memory4 = memory[:]
            memory4.append((cr, cc))
            helper(cr - 1, cc, length + 1, memory + [(cr, cc)])

    helper(sr, sc, 0, [])
    if res:
        return res[0]
    return -1

grid = [
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
        ]
sr, sc, tr, tc = 0, 0, 2, 0
test = shortestCellPath1(grid, sr, sc, tr, tc)
print(test == 6)