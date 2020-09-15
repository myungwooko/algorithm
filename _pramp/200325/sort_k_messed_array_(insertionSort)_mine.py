"""
K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer
"""


# 이경우 k는 Time complexity를 위해 줬다고 생각? 어쨌든 그만큼에 못간다는 걸 나타내준거니까.
# insertionSort Time: O(Nk), Space: O(1)
def sort_k_messed_array(arr, k):
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        # mine
        # keep comparing key and arr[j] as much as possible
        # greater one will change their place to the next step by step
        # when stopped replace the place with the key
        while j >= 0 and key < arr[j]:
            # at the start j+1 = i
            arr[j + 1] = arr[j]
            j -= 1
        # not greater => so just replace the last possible place with the key
        arr[j + 1] = key
    return arr


# Time complexity: O(n*k) => n is lenght of arr, k is k of the arguments
# Space complexity: O(1)
def sort_k_messed_array(arr, k):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            curr = i
            while curr > 0 and arr[curr - 1] > arr[curr]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
                curr -= 1
    return arr


# Time complexity: O(n*k)
# Space complexity: O(1)
def sort_k_messed_array(arr, k):
    for i in range(1, len(arr)):
        curr = i
        limit = curr - k
        while curr >= limit and curr > 0:
            if arr[curr] < arr[curr - 1]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
                curr -= 1
            else:
                break
    return arr


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
test = sort_k_messed_array(arr, k)
print(test)

test = sort_k_messed_array([1, 2, 4, 3, 5, 7, 6], 1)
print(test)
