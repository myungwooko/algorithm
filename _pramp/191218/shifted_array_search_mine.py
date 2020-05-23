"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it.
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr.
If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
Constraints:

[time limit] 5000ms
[input] array.integer arr
[input] integer num
[output] integer

try it: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
def get_pivot(shiftArr):
    pivot = 0
    for i, v in enumerate(shiftArr):
        if i + 1 < len(shiftArr) and shiftArr[i] > shiftArr[i + 1]:
            pivot = i
            break
    return pivot


def shifted_arr_search(shiftArr, num):
    l, r = 0, len(shiftArr) - 1
    while l <= r:
        mid = (l + r) // 2
        if shiftArr[mid] == num:
            return mid
        elif shiftArr[l] < shiftArr[mid]:
            if shiftArr[l] <= num < shiftArr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            l = mid + 1
    return -1


# more simple
# Time: O(logn)
# Space: O(1)
def shifted_arr_search(shiftArr, num):
    l, r = 0, len(shiftArr) - 1
    while l <= r:
        mid = (l + r) // 2
        if shiftArr[mid] == num:
            return mid

        if shiftArr[l] < shiftArr[mid]:
            if shiftArr[l] <= num < shiftArr[mid]:
                r = mid - 1
                continue
        l = mid + 1

    return -1


shiftArr = [5, 6, 7, 8, 1, 2, 3]
num = 2
test = shifted_arr_search(shiftArr, num)
print(test==5)

shiftArr = [0]
num = 0
test2 = shifted_arr_search(shiftArr, num)
print(test2==0)

"""
1. shiftArr = [9, 12, 17, 2, 4, 5], num = 2
               ^                ^         
                                       
2. shiftArr = [2, 4, 5 ,9 ,12 ,17], num = 2


l, h = 0, len(stiftArr)-1
m = (l+h)//2
-
get_pivot
arr = [7,8,9,1,2,3,4,5]
           ^
=> return 2
"""
