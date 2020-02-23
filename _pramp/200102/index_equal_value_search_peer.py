def index_equals_value_search(arr):
    arr.sort()
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == arr[mid]:
            return mid
        elif mid < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

















arr = [-8,0,2,5,9]
       # 0,1,2,3,4

# not working for upper example
print(1, index_equals_value_search(arr))
