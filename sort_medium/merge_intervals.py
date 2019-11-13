"""
56. Merge Intervals
Medium

Share
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

- overlapping => 겹치다. there are some same points.
- 앞의 수가 작은것 순으로 오름차순 정렬먼저
- 앞의[1]과 뒤의[0]을 통해 => 무관한지 겹치는지 속하는지 포함하는지를 판별
- 그렇게 순서대로 해나가면
"""

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        base = intervals[0]
        for i in range(1, len(intervals)):
            if base[1] < intervals[i][0]:
                res.append(base)
                base = intervals[i]
            else:
                base[0] = min(base[0], intervals[i][0])
                base[1] = max(base[1], intervals[i][1])
        res.append(base)
        return res

input = [[1,4],[0,5]]                     # => [[0, 5]]
input1 = [[1,3],[2,6],[8,10],[15,18]]     # =>  [[1,6],[8,10],[15,18]]
input2 = [[1,4],[4,5]]                    # => [[1,5]]
input3 = [[2,3],[4,5],[6,7],[8,9],[1,10]] # => [[1,10]]

s = Solution()
test = s.merge(input3)
print(test)