"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers
(quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order.
If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter
(considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer s

[output] array.integer
"""


# Time: O(n^3)
# Space: O(1)
def find_array_quadruplet(arr, s):
    arr.sort()
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            l, r = j + 1, len(arr) - 1
            while l < r:
                quad = [arr[i], arr[j], arr[l], arr[r]]
                sumQ = sum(quad)
                if sumQ == s:
                    return quad
                elif sumQ < s:
                    l += 1
                else:
                    r -= 1
    return []


# This is not about only return first one, return every possible combination
# When you want to skip same pick you can pass like this
def find_array_quadruplet(arr, s):
    arr.sort()
    result = []
    for i in range(len(arr)-3):
        if arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j != i+1 and arr[j] == arr[j-1]:
                continue
            l, r = j+1, len(arr) - 1
            while l < r:
                sum = arr[i] + arr[j] + arr[l] + arr[r]
                if sum  == s:
                    result.append([arr[i], arr[j], arr[l], arr[r]])
                    while l < r:
                        if arr[l] == arr[l+1]:
                            l += 1
                        else:
                            break
                    while l < r:
                        if arr[r] == arr[r-1]:
                            r -= 1
                        else:
                            break
                    l += 1
                    r -= 1
                elif sum < s:
                    l += 1
                else:
                    r -= 1
    return result


arr, s = [4, 4, 4, 4, 6, 2], 16
test = find_array_quadruplet(arr, s)
print(test)




