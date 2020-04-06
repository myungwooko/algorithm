"""
# [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
             !
          !
"""
def moveZerosToEnd(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i + 1, len(arr)):
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
    return arr


def moveZerosToEnd(arr):
    write = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1

    for j in range(write, len(arr)):
        arr[j] = 0

    return arr


# Time: O(N), Space: O(1)
def moveZerosToEnd(arr):
    write = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write], arr[i] = arr[i], arr[write]
            write += 1
    return arr

input = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
     #                                ^
test = moveZerosToEnd(input)
print(test)