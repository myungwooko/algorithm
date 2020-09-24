"""
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i
for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer
"""
""""Let us find the smallest element that the element itself and the index is same"""

# basically from some point, if value is greater than its index it's not possible to find matching one.


# O(N)
def index_equals_value_search(arr):
    if not arr or len(arr) > 100:
        return -1
    for i, v in enumerate(arr):
        if v > i:
            return -1
        if i == v:
            return i
    return -1


# Time Complexity: O(logn)
# Space Complexity: O(1)
def index_equals_value_search(arr):
    l, r = 0, len(arr) - 1

    while l <= r:  # <= "=" for [0] case only one element also has to be dealt with <================================= 중요
        mid = (l + r) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            r = mid - 1  # <= reason for the "-" is that we already know arr[mid] != mid, so we can except that and we should do that so that we and reduce the arrange
        else:
            l = mid + 1
    return -1


arr = [-8, 0, 2, 5]
test = index_equals_value_search(arr)
print(test)

# test -1, +1 with egg problem
top = 157
the_level = 93


def egg(the_level, top):
    count = 0
    l, r = 0, top

    while l <= r:
        mid = (l + r) // 2
        if mid == the_level:
            return count
        elif the_level < mid:
            r = mid - 1
        else:
            l = mid + 1
        count += 1

    return -1


test = egg(the_level, top)
print(test)
