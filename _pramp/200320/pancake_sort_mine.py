"""
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip
you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use
the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms
[input] array.integer arr
[input] integer k
0 ≤ k
[output] array.integer
"""
"""
We can place the largest element (in location i, 1-indexed) by flipping i to move the element to the first position,
then A.length to move it to the last position. Afterwards, the largest element is in the correct position, so we no longer need to pancake-flip by A.length or more.
We can repeat this process until the array is sorted. Each move will use 2 flips per element.

Simply,
- Biggest one -> move to first -> move to last
- Exclude that last one
- Repeat it till argument length is 0
"""


def flip(arr, k):
    l, r = 0, k
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


# Time complexity  O(n) x O(n) = o(n^2) helper function use O(n), and we call it n times.
# Space complexity O(1)
"""
a space complexity of O(1) means that the space required by the algorithm to process data is constant; it does not grow 
with the size of the data on which the algorithm is operating. Using only variable means O(1) 
"""


def pancake_sort(arr):
    def helper(arr, length):
        if not length:
            return

        big = max(arr[:length])  # need to exclude the finished one
        k = arr.index(big)
        flip(arr, k)
        flip(arr, length - 1)
        helper(arr, length - 1)

    helper(arr, len(arr))
    return arr


a = [2, 3, 41, 23, 4, 6]
print(pancake_sort(a))

"""
The reason for doing (s_idx+1 and k-1) two steps,
even though when two steps are done that will be equal to doing nothing, 
is the condition said flip's k is for first k element
"""


def flip(arr, k):
    l, r = 0, k - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


# Time complexity: O(n^2)
# Space complexity: O(n) <= in place is O(1) but here we used kind of O(n) space in the process for making sliced list.
def pancake_sort(arr):
    for i in range(len(arr)):
        sub = arr[i:]
        s_index = sub.index(min(sub))
        k = s_index + 1
        sub = flip(sub, k)
        arr[i:] = sub
    return arr


def flip(arr, k):
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# Time complexity: O(n^2)
# Space complxity: O(n) <= the most biggest one which is used additionally.
def pancake_sort(arr):
    for i in range(len(arr)):
        sliced = arr[i:]
        smallest = min(sliced)
        smallest_idx = sliced.index(smallest)
        arr[i:] = flip(sliced, smallest_idx + 1)
    return arr
