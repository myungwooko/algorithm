# Complete the 'movesToSolve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY puzzle as parameter.
#


# using queue => every possible candidates
# make positioned map
# when it matched return count
def movesToSolve(puzzle):
    positioned = []
    num = 0
    zero_start = False

    for r in range(len(puzzle)):
        row = []
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 0:
                zero_start = (r, c)
            row.append(num)
            num += 1
        positioned.append(row)

    p_map = {}
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            p_map[positioned[r][c]] = (r, c)

    queue = [(zero_start[0], zero_start[1], puzzle, [], 0)]
    while queue:

        r, c, curr_puzzle, seen, count = queue.pop(0)

        if curr_puzzle == positioned:
            return count

        candidates = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for r1, c1 in candidates:
            if 0 <= r1 < len(positioned) and 0 <= c1 < len(positioned[0]):
                if p_map[curr_puzzle[r][c]] == (r1, c1):
                    continue
                copied = []

                for row in puzzle:
                    copied.append(row[:])

                copied[r][c], copied[r1][c1] = copied[r1][c1], copied[r][c]

                if copied not in seen:
                    queue.append((r1, c1, copied, seen + [copied], count + 1))

    return


import collections


def slidingPuzzle(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    R, C = len(board), len(board[0])
    start_list = []
    for i in range(0, R):
        start_list += board[i]
    start = tuple(start_list)
    target = tuple(range(1, R * C) + [0])
    start_idx = start.index(0)
    queue = collections.deque([(start, start_idx, 0)])
    visited = {start}

    while queue:
        state, pos, depth = queue.popleft()
        if state == target:
            return depth
        for d in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            r, c = pos / C, pos % C
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < R and 0 <= nc < C:
                npos = nr * C + nc
                nstate = list(state)
                nstate[pos], nstate[npos] = nstate[npos], nstate[pos]
                nstate = tuple(nstate)
                if nstate not in visited:
                    visited.add(nstate)
                    queue.append((nstate, npos, depth + 1))

    return -1


puzzle = [[1, 3, 4], [2, 5, 0], [6, 8, 7]]
test = slidingPuzzle(puzzle)
print(test)
