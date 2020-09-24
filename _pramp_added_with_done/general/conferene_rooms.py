"""
Given an array of meeting time intervals consisting of  start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required. Example 1: Input: [[0, 30],[5, 10],[15, 20]] Output: 2
"""


def rooms(arr):
    if not arr:
        return 0
    rooms = [arr[0]]
    for idx in range(1, len(arr)):
        i, j = arr[idx]
        idx2 = 0
        extended = False
        before = len(rooms)
        while idx2 < len(rooms):
            s, e = rooms[idx2]
            if j <= s or i >= e:
                rooms[idx2] = [min(s, i), max(j, e)]
                extended = True
                break
            idx2 += 1
        if not extended and len(rooms) == before:
            rooms.append([i, j])
    return len(rooms)


arr = [[10, 15], [9, 11], [12, 15], [18, 20], [16, 19], [9, 10], [18, 23]]
print(rooms(arr))
