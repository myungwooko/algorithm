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


# Time O(NK) <- condition gave us already
# Space O(1)
def sort_k_messed_array(arr, k):
    idx = 1
    while idx < len(arr):
        while idx - 1 >= 0 and arr[idx] < arr[idx - 1]:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1
        idx += 1
    return arr


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
test = sort_k_messed_array(arr, k)
print(test)

test = sort_k_messed_array([1,2,4,3,5,7,6], 1)
print(test)

