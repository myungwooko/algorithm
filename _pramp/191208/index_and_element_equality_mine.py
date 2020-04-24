"""Let us find the smallest element that the element itself and the index is same"""
#basically from some point, if value is greater than its index it's not possible to find matching one from that point.

# basically from some point, if value is greater than its index it's not possible to find matching one.


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


# Time: O(logN)
# Space: O(N) <= every element is same with each's index
def index_equals_value_search(arr):
    res = []
    l, r = 0, len(arr)
    # "=" for [0] case only one element has to deal with <============================================================== 중요
    while l <= r:
        mid = (l + r) // 2  # 괄호! <==================================================================================== 중요
        if arr[mid] >= mid:
            if arr[mid] == mid:
                res.append(mid)
            # 경우에 따른 -1, +1의 이유는 이제 해당 mid는 아닌게 분명하므로 제외하는 것 <============================================== 중요
            # why -1,+1 along the cases => that mid value has to be excluded, so we do +1 or -1 for doing that
            r = mid - 1
        else:
            l = mid + 1
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


arr = [-8,0,2,5]
test = index_equals_value_search(arr)
print(test)



# test -1, +1 with egg problem
top = 157
the_level = 93


def egg(the_level, top):
    count = 0
    l, r = 0, top

    while l <= r:
        mid = (l + r) // 2
        if mid == the_level:
            return count
        elif the_level < mid:
            r = mid - 1
        else:
            l = mid + 1
        count += 1

    return -1


test = egg(the_level, top)
print(test)


