"""
253. Meeting Rooms II
Medium


Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number
of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            # 맨 앞(가장 작은것)이랑만 비교하면 된다. 그게 가장 큰 선택지를 놓고 고르는 것이므로 거기서만 안걸려도 들어갈데가 있다는 #             말이 되니깐. 즉 다른거랑 비교해서 걸려도 가장 폭넓은 선택지가 있는 이곳에서만 안걸리게 되면 오케이 인것.
            if heap and i[0] >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)

    # same just cleaner
    def minMeethingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for time in intervals:
            if heap and heap[0] <= time[0]:
                heapq.heapreplace(heap, time[1])
            else:
                heapq.heappush(heap, time[1])
        return len(heap)


