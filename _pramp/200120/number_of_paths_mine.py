"""
Grid 문제 dp
grid 경로 문제에서(대각선 이동 불가능 전제)


0 . 0 . 0 . 5
0 . 0 . 2 . 5
0 . 1 . 2 . 3
1 . 1 . 1 . 1


어느 지점 b로 오는 것을 두개의 누적경로 값(a, d)을 그냥 더하면 되는 이유는
b까지의 경로는 a까지의 경로 + d까지의 경로
 a b
 c d
조건상 해당 두 지점에서 밖에 올수 없는데
각각의 지점 까지 온 개수의 합을 하면 그게 b까지 오는 지점이 된다.
왜냐면 b까지는 해당 두지점으로부터 밖에 올수 없고,
두 지점까지의 경로의 개수가 각각 그것이므로.

* 누적 값의 합에 의해 변경해주는 순서는 Row by Row 헷갈리지 말 것.
* 처음에 모서리에 1을 깔아주는 이유는 그곳은 대각선이 아니므로 그곳으로 오는 두지점이란게 존재하지 않고,
 오로지 그곳으로의 하나의 경로만 있기 떄문에 base로 깔아주는 것.


아래의 문제에선 조건이 하나 더있다. y(column) >= x(row) 여야만 한다.
각각의 문제의 조건을 잘 확인할 것.
"""
"""
Attention:
Explanation's (i, j) referring (col, row) => So, that can be translated to => (i >= j) == (col >= row)  

(i)------->   
  x x x x |
  x x x x |
  x x x x |
  x x x x V
          (j)

# set 1 all of the first i line except the starting point
# That's because the way of each point of the line is only one
# Then we will go to every point we can(by the constrint >=j) and then we will add up its (i-1) and (j-1)
# Then we can just simply return the last one
"""


def num_of_paths_to_dest(n):
    if n == 1:
        return 1

    dp = [[0] * n for _ in range(n)]
    dp[0] = [1] * n
    dp[0][0] = 0

    for row in range(n):
        for col in range(n):
            if row > 0 and col > 0 and col >= row:
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

    return dp[-1][-1]


"""
 0 1 1 1 
 0 1 2 3 
 0 0 2 5
 0 0 0 5 
"""

# (column,row)
# Condition:
# 1: i >= j => x >= y
# 2: it cannot cross the diagonal border


# Time Complexity: O((n-1)^2)
# Space Complexity: O(n^2)
def num_of_paths_to_dest(n):
    dp = [[0] * n for r in range(n)]
    dp[0] = [1] * n
    # Why did not change for every first element of every row to 1?
    # Because by the condition 1, the car can't reach out there.
    for r in range(1, n):
        for c in range(1, n):
            if c >= r:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[n - 1][n - 1]
