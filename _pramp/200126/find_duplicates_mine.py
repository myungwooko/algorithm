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
"""
sorted
[1,2,3,4,5]
[3,4,5]

 M ≈ N - the array lengths are approximately the same M ≫ N - 
 arr2 is much bigger than arr1.

time = O(MN), space = O(M+N)

go thru both at once
time = O(m+n) space = O(m+n)


[1,2,3,4,5], [4,5,6,7]
 i           j


loop (while i < len(arr1) and j < arr2)

"""
"""
sorted
[1,2,3,4,5]
[3,4,5]

 M ≈ N - the array lengths are approximately the same M ≫ N - 
 arr2 is much bigger than arr1.

time = O(MN), space = O(M+N)

go thru both at once
time = O(m+n) space = O(m+n)


[1,2,3,4,5], [4,5,6,7]
 i           j


loop (while i < len(arr1) and j < arr2)

"""
"""
sorted
[1,2,3,4,5]
[3,4,5]

 M ≈ N - the array lengths are approximately the same M ≫ N - 
 arr2 is much bigger than arr1.

time = O(MN), space = O(M+N)

go thru both at once
time = O(m+n) space = O(m+n)


[1,2,3,4,5], [4,5,6,7]
 i           j


loop (while i < len(arr1) and j < arr2)

"""
# Time complexity: O(n+m)
# Space complexity: O(min(n, m))
def find_duplicates(arr1, arr2):
    l = r = 0
    result = []
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            l += 1
        elif arr2[r] < arr1[l]:
            r += 1
        else:
            result.append(arr1[l])
            l += 1
            r += 1
    return result


# Time complexity: O(n+m)
# Space compexity: O(min(n, m))
def find_duplicates(arr1, arr2):
    left_idx = right_idx = 0
    res = []
    while left_idx < len(arr1) and right_idx < len(arr2):
        left = arr1[left_idx]
        right = arr2[right_idx]
        if left < right:
            left_idx += 1
        elif left > right:
            right_idx += 1
        else:
            res.append(left)
            left_idx += 1
            right_idx += 1
    return res
