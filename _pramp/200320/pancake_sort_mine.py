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





