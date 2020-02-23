# Just a information, basically from some point, if value is greater than its index it's not possible to find matching one.
# if arr's every element is not repeated and arr is sorted in order of ascending


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

# O(logN)
def index_equals_value_search(arr):
    lo, hi = 0, len(arr) - 1
    candidates = []
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] >= mid:
            if mid == arr[mid]:
                candidates.append(mid)
            hi = mid - 1
        else:
            lo = mid + 1

    if candidates:
        return candidates[-1]
    return -1














































"""
 arr = [-8,0,2,5,9]
         0,1,2,3,4

lo    0 
hi    4
m     2
a[m]  2 
"""








