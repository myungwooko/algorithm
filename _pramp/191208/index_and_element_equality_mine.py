"""Let us find the smallest element that the element itself and the index is same"""
#basically from some point, if value is greater than its index it's not possible to find matching one from that point.

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
    res = []
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if arr[mid] >= mid:
            if arr[mid] == mid:
                res.append(mid)
            hi = mid - 1
        else:
            lo = mid + 1
    if res:
        return res[-1]
    return -1

"""
 arr = [-8,0,2,5,9]
         0,1,2,3,4
lo    0 
hi    4
m     2
a[m]  2 
"""

input = [-8,0,2,5,9]
test = index_equals_value_search(input)
print(test)