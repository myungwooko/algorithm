"""
Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of
all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions:
M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
output: [3, 6, 7]
"""
"""
go thru both at once
time = O(m+n) space = O(m+n)


[1,2,3,4,5], [4,5,6,7]
 i           j

loop (while i < len(arr1) and j < arr2)
"""
# time O(MN), space O(M+N)
def find_duplicates(arr1, arr2):
    N = len(arr1)
    M = len(arr2)
    longer = arr1
    shorter = arr2
    if M - N > 0:
        longer, shorter = arr2, arr1

    res = []
    for i in longer:
        if i in shorter:
            res.append(i)

    return res


# Time max O(M+N),
# Space O(M+N) => 다 똑같을 수도 있는 거니까
def find_duplicates(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1
    return result


