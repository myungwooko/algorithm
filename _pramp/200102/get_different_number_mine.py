"""
# have to find none negative integer
# we are not sure the array is sorted

time O(NlogN), space O(1)
"""
def get_different_number(arr):
    arr.sort()
    smallest = arr[0]
    if smallest:  # => not zero
        return 0
    else:
        for i in range(len(arr) - 1):
            if arr[i] + 1 != arr[i + 1]:
                return arr[i] + 1
        return arr[-1] + 1


def get_different_number(arr):
    arr.sort()
    res = 0
    for i in arr:
        if i == res:
            res += 1
    return res


a = [1, 2, 3, 4, 5]
print(get_different_number(a))


#time O(N), space O(N)
"""
set: x in s  => O(1), Average worst O(n)
list x in li => O(n), Average 
* 그러한 이유로 아래의 알고리즘이 list 인 상태에서 그냥 진행하진 않고 set을 사용하는 것이다.  
"""
def getDifferentNumber(arr):
   n = len(arr)
   collection = set()
   for i in range(n):
       collection.add(arr[i])

   for i in range(n):
       if i not in collection:
           return i

a = [0, 2, 3, 4, 5]
print(getDifferentNumber(a))


sdlkfmal




