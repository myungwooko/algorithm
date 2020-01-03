def index_equals_value_search(arr):
    result = len(arr)
    for i in range(len(arr)):
        if arr[i] == i:
            result = i  #=> return i?
            break
    return result if result != len(arr) else -1 #return -1

#Binary search => not working
def index_equals_value_search(arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
    if arr[mid] == mid:
        r = mid - 1
    else:
        l = mid + 1
    return l if l < len(arr) else -1

arr = [-8,0,2,5,9]
       # 0,1,2,3,4

# not working for upper example
print(1, index_equals_value_search(arr))
