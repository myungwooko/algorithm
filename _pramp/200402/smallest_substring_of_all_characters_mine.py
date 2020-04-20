"""
Brute force
- Time complexity => O(n^2*m*k) => n is length of str, m is length of arr, k is temp acc's length
=> in here, k will definitely always small than str we can eliminate it
=> So Time complexity: O(n^2*m)
=> Space complexity: O(m), m is length of arr because we made elements set 
"""


def get_shortest_unique_substring(arr, str):
    elements = set(arr)
    res = ""
    for i in range(len(str)):
        acc = ""
        acc += str[i]
        if set(acc) == elements:
            return acc
        for j in range(i + 1, len(str)):
            acc += str[j]
            if set(elements).issubset(set(acc)):
                if not res or len(res) > len(acc):
                    res = acc
                    print(1, res)
                    break
    return res



"""
- till finding valid substring make length longer
- valid means substring has to include every characters in arr
- till finding valid -> make longer, using right
- till searching the new smallest -> make shorter, using left
- when our left arrive the index which can make the length of the array from the point

Time: those functions like is subset makes it multiplies time complexity
and it is not really simple and clear

Space: O(m+k) and is  not really simple and clear
"""
from collections import Counter


def get_shortest_unique_substring(arr, str):
    res = ""
    countMap = Counter(arr)

    for l in range(len(str) - len(arr) + 1):
        r = l + len(arr) - 1
        frac = Counter(str[l:r + 1])
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
    return res




"""
I got it!
- Using l, r
- r all inclusive
- we ignore for not icluded char for the arr
- l increment till meet the smallest for the range
- then l will be out of bound because it doesn't satisfy while loop last
- our map calculated all in and out 
- we start right increment again till it would be all inclusive
- then we repeat all the logic we did
- then return the smallest one

# map을 만들어서 사용하는 이유는 => set을 만들고 비교하거나 리스트로 비교하거나 어쩄든 같은지 비교하려면 비교할떄마다 O(N)
# map 만들고 count 만들어서 하면 필요한 비교만 딱 가능.
"""


# Time complexity O(N+M) <= in the case, we don't know what is the greater one for N and M we can write exactly what it is
# Space complexity O(N) N is length of arr
def get_shortest_unique_substring(arr, str):
    l = 0
    map_c = {}
    unique_counter = 0
    res = ""

    for e in arr:
        map_c[e] = 0

    for r in range(len(str)):
        if str[r] not in map_c:
            continue

        if map_c[str[r]] == 0:
            unique_counter += 1

        map_c[str[r]] += 1

        while len(arr) == unique_counter:
            temp_length = r - l + 1
            if temp_length == len(arr):
                return str[l:r + 1]

            if not res or len(res) > temp_length:
                res = str[l:r + 1]

            head_char = str[l]

            if head_char in map_c:
                map_c[head_char] -= 1
                if map_c[head_char] == 0:
                    unique_counter -= 1

            l += 1

    return res

