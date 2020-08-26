"""
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference
that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer
"""
# brute force
def find_pairs_with_given_difference(arr, k):
    dic = {}
    for i in range(len(arr)):
        dic[arr[i]] = i

    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] - arr[j] == k:
                pairs.append([arr[i], arr[j]])

    result = sorted(pairs, key=lambda x: arr.index(x[1]))

    return result


"""
why this is diffrent with twoSum problem?
This is not different from simple twoSum problem
twoSum just return when it found the pair satisfies the condition
but this problem need to return all of pairs
one element can be x in a pair and can be y in another pair
"""
# y = x - k
# Time complexity: O(n)
# Space complexity: O(n)
def find_pairs_with_given_difference(arr, k):
    mapper = {}
    for x in arr:
        y = x - k
        mapper[y] = x

    res = []
    for y in arr:
        if y in mapper:
            x = mapper[y]
            res.append([x, y])

    return res


