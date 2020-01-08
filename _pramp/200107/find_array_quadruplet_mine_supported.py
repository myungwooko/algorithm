# peers
# O(n^2LogN)
# def find_array_quadruplet(arr, s):
    # if len(arr) < 4:
    #     return []
    # arr.sort()
    # for i in range(0, len(arr) - 3):
    #     # doesn't need to check about same case
    #     if i > 0 and arr[i] == arr[i - 1]:
    #         continue
    #     for j in range(i + 1, len(arr) - 2):
    #         # doesn't need to check about same case
    #         if j > i + 1 and arr[j] == arr[j - 1]:
    #             continue
    #         # two pointer => smallest one, and biggest one
    #         k = j + 1
    #         l = len(arr) - 1
    #         while k < l:
    #             tempSum = arr[i] + arr[j] + arr[k] + arr[l]
    #             if tempSum == s:
    #                 return [arr[i], arr[j], arr[k], arr[l]]
    #             elif tempSum < s:
    #                 k += 1
    #             else:
    #                 l -= 1
    #     return []


# mine
def find_array_quadruplet(arr, s):
    if len(arr) < 4:
        return []
    arr.sort()
    for i in range(len(arr) - 3):
        j = i + 1
        while j < len(arr) - 2:
            l, r = j + 1, len(arr) - 1
            while l < r:
                tmpSum = arr[i] + arr[j] + arr[l] + arr[r]
                if tmpSum < s:
                    l += 1
                elif tmpSum > s:
                    r -= 1
                else:
                    return [arr[i], arr[j], arr[l], arr[r]]
            j += 1
    return []

arr, s = [4, 4, 4, 2], 16
test = find_array_quadruplet(arr, s)
print(test)




