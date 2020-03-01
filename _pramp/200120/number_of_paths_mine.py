"""
Number of Paths
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. The car is supposed
to get to the opposite, Northeast (top-right), corner of the grid. Given n, the size of the grid’s axes, write a function
numOfPathsToDest that returns the number of the possible paths the driverless car can take.

For convenience, let’s represent every square in the grid as a pair (i,j). The first coordinate in the pair denotes the east-to-west axis,
and the second coordinate denotes the south-to-north axis. The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border. In other words, in every step the position (i,j)
 needs to maintain i >= j. See the illustration above for n = 5. In every step, it may go one square North (up), or one square East (right),
 but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.

Example:

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)
Constraints:

[time limit] 5000ms

[input] integer n

1 ≤ n ≤ 100
[output] integer
"""


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
# Eventually the picture is picture as a abstraction for making understanding well.
# We can implement it as we are comfortable, keeping that basic concept.
def num_of_paths_to_dest(n):
    dp = [[0]*n for _ in range(n)]
    dp[0] = [1]*n
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if j >= i:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

test = num_of_paths_to_dest(4)
print(test)

