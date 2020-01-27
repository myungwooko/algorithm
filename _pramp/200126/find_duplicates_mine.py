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


# time O(M+N), space O(M+N) => 다 똑같을 수도 있는 거니까def find_duplicates(arr1, arr2):
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



