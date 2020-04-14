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


# x-y = k  =>  y = x-k
# order of y in arr
def find_pairs_with_given_difference(arr, k):
    pairs = []
    map1 = {}
    for x in arr:
        map1[x - k] = x

    for y in arr:
        if y in map1:
            pairs.append([map1[y], y])
    return pairs
