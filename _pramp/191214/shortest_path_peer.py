import unittest


#peer's => good access, answer is not right though
def shortestCellPath(grid, sr, sc, tr, tc):
    """
    BEAT.IO

    Input:
    Output:
    Brute Force:
    EdgeCases:  => Hadling exception
    Assumptions: => 생각의 정리 확인 과정.
    Toolbox: => the idea you use
      for array -> 2 pointers, hashtables
      for linkedlist -> 2 pointers, hashtables
      for tree/graph -> dfs/bfs/topological sort

    Input : grid
          (start_row, start_col), (end_row, end_col)

    Output : int -> represents the shortest path between the 2 coordinates
          -> WAlk through the grid
          -> All walking paths must be 1

    Assumptions:
    -> (start_row, start_col), (end_row, end_col) = 1
    -> All values in the grid are either 0 or 1
    -> There may not be a valid path
      -> return - 1
    -> We can walk
      up,      -> row - 1
      down,    -> row + 1
      right,   -> col + 1
      left     -> col - 1

    Brute Force:
    -> Try every single path and then return the minimum path

    Toolbox:
    -> Iterative BFS
    -> Graph Traversal Problem (Adjacency Matrix)
    """
    if not grid:
        return -1

    # Initailize BFS variables
    queue = [(sr, sc)]
    count = 0
    seen = set()
    # While Queue
    while queue:
        current = queue.pop(0)
        curr_row, curr_col = current
        if (curr_row, curr_col) not in seen and 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0]) and \
                grid[curr_row][curr_col] == 1:
            seen.add((curr_row, curr_col))
            # Go up
            queue.append((curr_row - 1, curr_col))
            # Go Down
            queue.append((curr_row + 1, curr_col))
            # Go Left
            queue.append((curr_row, curr_col - 1))
            # Go right
            queue.append((curr_row, curr_col + 1))

            count += 1
            if (curr_row, curr_col) == (tr, tc):
                return count - 1
    return -1

# make routine
class TestSolution(unittest.TestCase):
    def test_one(self):
        grid = [[1, 1, 1, 1],
                [0, 1, 0, 1],
                [1, 1, 1, 1]]

        sr = 0
        sc = 0
        tr = 2
        tc = 0

        self.assertEqual(shortestCellPath(grid, sr, sc, tr, tc), 8)


if __name__ == '__main__':
    unittest.main()