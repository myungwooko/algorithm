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
"""
# [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
             !
          !
"""


# Time complexity: O(n)
# Space complexity: O(1)
def moveZerosToEnd(arr):
    write = idx = 0
    while idx < len(arr):
        if arr[idx]:
            arr[write], arr[idx] = arr[idx], arr[write]
            write += 1
        idx += 1
    return arr


test = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
print(moveZerosToEnd(test) == [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0])
