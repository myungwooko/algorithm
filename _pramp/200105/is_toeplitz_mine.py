"""
Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr,
write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]

is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

isn’t a Toeplitz matrix, so we should return false.

Constraints:

[time limit] 5000ms
[input] array.array.integer arr
0 ≤ arr.length ≤ 20
0 ≤ arr[i].length ≤ 20
0 ≤ arr[i][j] ≤ 20
[output] boolean
"""


# Time: O((m-1)*(n-1))
# Space: O(1)
def isToeplitz(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
      if arr[i][j] != arr[i+1][j+1]:
        return False
  return True


def isToeplitz(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
      r = i + 1
      c = j + 1
      while r < len(arr) and c < len(arr[0]):
        if arr[r][c] != arr[i][j]:
          return False
        r += 1
        c += 1
  return True


arr =[[1,2,3,4],
      [5,1,2,3],
      [6,5,1,2]]

print(isToeplitz(arr))





























