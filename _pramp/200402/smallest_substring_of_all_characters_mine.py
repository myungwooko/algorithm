from collections import Counter


# def get_shortest_unique_substring(arr, str):
#     l = 0
#     r = l + len(str) - 1
#     res = ""
#     countMap = Counter(arr)
#     while l <= len(str) - len(arr):
#         frac = Counter(str[l:r + 1])
#         print("frac", frac, l)
#         count = 0
#         for k in frac:
#             if k in countMap and frac[k] >= countMap[k]:
#                 count += 1
#         if count != len(countMap):
#             r += 1
#         else:
#             if not res or str[l:r + 1] < len(res):
#                 res = str[l:r + 1]
#             l += 1
#     return res

def get_shortest_unique_substring(arr, str):
    res = ""
    countMap = Counter(arr)

    for l in range(len(str)-len(arr)+1):
        r = l + len(arr) - 1
        frac = Counter(str[l:r+1])
        while r < len(str) and not set(countMap.keys()).issubset(frac.keys()):
            r += 1
            if r < len(str):
                if str[r] in frac:
                    frac[str[r]] += 1
                else:
                    frac[str[r]] = 1
            else:
                break

        # Because including r makes set(countMap.keys()).issubset(frac.keys()) to True => :r+1 is right
        while l < len(str) and set(countMap.keys()).issubset(frac.keys()):
            if not res or (len(res) > len(str[l:r + 1])):
                res = str[l:r + 1]
            frac[str[l]] -= 1
            if frac[str[l]] == 0:
                del frac[str[l]]
            l += 1
            # if not (l < len(str)):
            #     l -= 1
            #     break
    return res

arr = ['x','y','z']
st = "xyyzyzyx"
# arr = ["A"]
# st = "B"
res = get_shortest_unique_substring(arr, st)
print(res)