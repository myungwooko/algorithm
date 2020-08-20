"""
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer
"""


# Brute force
# Time O(n^2)
# Space O(n)
# keyword = 축적값
def array_of_array_products(arr):
    res = []
    if len(arr) <= 1:
        return res
    for i in range(len(arr)):
        multiplied = 1
        for j in range(len(arr)):
            if j == i:
                pass
            else:
                multiplied *= arr[j]
        res.append(multiplied)
    return res


def array_of_array_products(arr):
    if len(arr) == 1:
        return []
    cumulative = [1]
    acc = 1
    for i in range(len(arr) - 1):
        acc *= arr[i]
        cumulative.append(acc)

    arrSec = arr[::-1]
    print(1, cumulative, arrSec)
    cumulativeRev = [1]
    acc = 1
    for i in range(len(arr) - 1):
        acc *= arrSec[i]
        cumulativeRev.append(acc)
    print(2, cumulative, cumulativeRev)
    res = []
    for i in range(len(arr)):
        e1 = cumulative[i]
        e2 = cumulativeRev[-(i + 1)]
        res.append(e1 * e2)

    return res


"""
 # arr = [2,          7,          3,          4]
 # new = [7 * 3 * 4,  2 * 3 * 4,  2 * 7 * 4,  2 * 7 * 3]

 # 2 -> [1]       - [7, 3, 4]
 # 7 -> [2]       - [3, 4]
 # 3 -> [2, 7]    - [4]
 # 4 -> [2, 7, 3] - [1]


=========================================================== 
 1 7x3x4x1  1x2 3x4x1, 1x2x7 4x1, 1x2x7x3 1
 l     r      l   r     l     r    l      r

=> We need to make 
l = [1, 1x2, 1x2x7, 1x2x7x3]
r = [1, 1x4, 1x4x3, 1x4x3x7]

=> then reverse r
=> and then just multiply it
"""


# Time complexity: O(n)
# Space complexity: O(n)
def array_of_array_products(arr):
    if len(arr) <= 1:
        return []

    left_acc = [1]
    right_acc = [1]

    for i in range(0, len(arr) - 1):
        tmp = left_acc[-1] * arr[i]
        left_acc.append(tmp)

    for i in range(len(arr) - 1, 0, -1):
        tmp = right_acc[0] * arr[i]
        right_acc.insert(0, tmp)

    # result to left
    for i in range(len(arr)):
        left_acc[i] *= right_acc[i]

    return left_acc
