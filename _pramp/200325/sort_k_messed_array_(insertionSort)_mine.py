# Ans says from 1 to n is basic condition and used heap's efficiency for extraction => if there is k element => log(k)

# mine Time: O(Nk), Space: O(N)
def sort_k_messed_array(arr, k):
    sub = []
    i = 0
    while i < len(arr):
        if sub and sub[-1] > arr[i]:
            if len(sub) < k:
                start = 0
            else:
                start = len(sub) - k
            for sub_idx in range(start, len(sub)):
                if sub[sub_idx] >= arr[i]:
                    sub.insert(sub_idx, arr[i])
                    # for "for loop"
                    break
        else:
            sub.append(arr[i])
        i += 1
    return sub


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


test = sort_k_messed_array([1,2,4,3,5,7,6], 1)
print(test)

