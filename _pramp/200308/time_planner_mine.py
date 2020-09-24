"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur,
returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement,
return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC,
Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two.
The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot.
The input variable dur is a positive integer that represents the duration of a meeting in seconds.
The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed,
i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12
Constraints:

[time limit] 5000ms

[input] array.array.integer slotsA

1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB

1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer

[output] array.integer
"""


# Time O(NM)
def meeting_planner(slotsA, slotsB, dur):
    for i, s1 in enumerate(slotsA):
        for j, s2 in enumerate(slotsB):
            # Overlapping part => max of starts, min of ends*
            maxStart = max(s1[0], s2[0])
            minEnd = min(s1[1], s2[1])

            if minEnd <= maxStart:
                continue

            candidate = [maxStart, minEnd]

            if candidate[1] - candidate[0] >= dur:
                return [candidate[0], candidate[0] + dur]
    return []


"""
- if didn't make the answer we can increment index of time slots that has smaller end between comparing slots 
- Because two slots are already sorted and samller end can be possibly connected to smaller next start.
"""


# Time O(N+M)
def meeting_planner(slotsA, slotsB, dur):
    a = b = 0

    while a < len(slotsA) and b < len(slotsB):
        start = max(slotsA[a][0], slotsB[b][0])
        end = min(slotsA[a][1], slotsB[b][1])

        if start < end and end - start >= dur:
            return [start, start + dur]

        # 작으면 해당 슬롯에서 다음것으로 넘겼을때 그 다음것의 끝나는 시간이 범위 안에 들어가는 것일수도 있고
        # 거기서 또 해당 범위를 찾을수도 있는 거니까 그런식으로 하나씩 넘겨준다.
        # 이것은 O(n+m)이고 O(n*m)보다 훨씬낫다.

        # after checking the range is exist,
        # when one time block's ending time is smaller than other's ending time
        # we can make comparison with its next one.
        # That make time complexity O(n+m) and this is better than O(n*m)
        if slotsA[a][1] < slotsA[b][1]:
            a += 1
        else:
            b += 1

    return []


# Time Complexity: O(n+m)
# Space Complexity: O(1)
def meeting_planner(slotsA, slotsB, dur):
    idx_a = 0
    idx_b = 0
    while idx_a < len(slotsA) and idx_b < len(slotsB):
        common_start = max(slotsA[idx_a][0], slotsB[idx_b][0])
        common_end = min(slotsA[idx_a][1], slotsB[idx_b][1])

        if common_end - common_start >= dur:
            return [common_start, common_start + dur]

        if slotsA[idx_a][1] < slotsB[idx_b][1]:
            idx_a += 1
        else:
            idx_b += 1
    return []


# Time complexity: O(n+m)
# Space complexity: O(1)
def meeting_planner(slots_a, slots_b, dur):
    a = b = 0
    while a < len(slots_a) and b < len(slots_b):
        curr_a = slots_a[a]
        curr_b = slots_b[b]
        start = max(curr_a[0], curr_b[0])
        end = min(curr_a[1], curr_b[1])
        if end - start >= dur:
            return [start, start + dur]
        if curr_a[1] < curr_b[1]:
            a += 1
        else:
            b += 1
    return []


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
#output: [60, 68]
test = meeting_planner(slotsA, slotsB, dur)
print(test)
