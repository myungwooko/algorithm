"""
We can place the largest element (in location i, 1-indexed) by flipping i to move the element to the first position,
then A.length to move it to the last position. Afterwards, the largest element is in the correct position, so we no longer need to pancake-flip by A.length or more.
We can repeat this process until the array is sorted. Each move will use 2 flips per element.

Simply,
- Biggest one -> move to first -> move to last
- Exclude that last one
- Repeat it till argument length is 0
"""
def flip(arr, k):
    l, r = 0, k
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

# Time complexity  O(n) x O(n) = o(n^2) helper function use O(n), and we call it n times.
# Space complexity O(1)
"""
a space complexity of O(1) means that the space required by the algorithm to process data is constant; it does not grow 
with the size of the data on which the algorithm is operating. Using only variable means O(1) 
"""
def pancake_sort(arr):
    def helper(arr, length):
        if not length:
            return

        big = max(arr[:length]) #need to exclude the finished one
        k = arr.index(big)
        flip(arr, k)
        flip(arr, length-1)
        helper(arr, length-1)

    helper(arr, len(arr))
    return arr

a = [2, 3, 41, 23, 4, 6]
print(pancake_sort(a))


# Peer's without additional information of Pancake sort
def flip(arr, k):
    '''
    k = 2
    arr =  [1, 2, 3, 4, 5]
    out =  [2  1  3  4  5]
    '''
    start = 0
    end = k
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Time O(n^2) including counting flip's time complexity
# Space O(1)
def pancake_sort(arr):
    # find the smallest elem at iteration k
    start = 0
    while start <= len(arr) - 2:
        subarr = arr[start:]
        idx = subarr.index(min(subarr))
        subarr = flip(subarr, idx)
        arr[start:] = subarr
        start += 1
    return arr


arr = [1, 5, 4, 3, 2]
print(pancake_sort(arr))


"""
The reason for doing (s_idx+1 and k-1) two steps,
even though when two steps are done_with_pramp that will be equal to doing nothing, 
is the condition said flip's k is for first k element
"""
def flip(arr, k):
    l, r = 0, k-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


def pancake_sort(arr):
    for i in range(len(arr)):
        sub = arr[i:]
        s_idx = sub.index(min(sub))
        ordered = flip(sub, s_idx+1)
        arr[i:] = ordered
    return arr

arr = [1, 5, 4, 3, 2]
print(pancake_sort(arr))

