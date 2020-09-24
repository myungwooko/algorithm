"""
539. Minimum Time Difference
Medium

Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""


class Solution:
    def findMinDifference(self, timePoints):
        # sorted makes every element to be right next with their partners who makes the smallest diffrence with themselves
        timePoints = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timePoints])

        # because only that difference of first one and last one was excluded in the calculation.
        timePoints.append(1440 + timePoints[0])
        return min((b - a for a, b in zip(timePoints, timePoints[1:])))


S = Solution()
input = ["23:59", "00:00"]
test = S.findMinDifference(input)
print(test)
