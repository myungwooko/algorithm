"""
Move Zeros To End
Given a static-sized array of integers arr, move all zeroes in the array to the end of the array.
You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

Examples:

input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
Constraints:

[time limit] 5000ms
[input] array.integer arr
0 ≤ arr.length ≤ 20
[output] array.integer
"""
"""
# [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
             !
          !
"""
# Brute force
def moveZerosToEnd(arr):
  for i in range(len(arr)):
    if arr[i] == 0:
      for j in range(i+1, len(arr)):
        if arr[j] != 0:
          arr[i], arr[j] = arr[j], arr[i]
          break
  return arr


# Time Complexity: O(n)
# Space Complexity: O(1)
def moveZerosToEnd(arr):
  write = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[write], arr[i] = arr[i], arr[write]
      write += 1
  return arr


input = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
     #                                ^

test = moveZerosToEnd(input)
print(test)
