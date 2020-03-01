"""
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

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
key point
* Why its approach is different with Two sum => x, y's different order can be possibly pair even though reverse order can't be.

   x-y = k 
=> y = x-k
1. first for loop => dict with dict[x-k] = x 
다음 for loop에서 순서대로 돌면서 y로서 존재한다면 바로 key로서 조회할수 있도록.
=> 결론적으론 dic[y] = x

2. second for loop => 자신을 y로서 조회 vlaue가 해당 연산으로서의 x로서 존재 하는 것이므로. pair = [dict[key], key]
*순서대로 돌면서 접근하므로 y에 대한 index순서로서의 pairs를 자연적으로 갖게 된다.
Time O(N), Space O(2N) => O(N)
"""


def find_pairs_with_given_difference(arr, k):
    pairs = []
    hashMap = {}
    for num in arr:
        hashMap[num - k] = num
    for num in arr:
        if num in hashMap:
            pairs.append([hashMap[num], num])
    return pairs
