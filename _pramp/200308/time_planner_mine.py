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

        # Bc smaller's next has more possibility to have smaller start
        if slotsA[a][1] < slotsA[b][1]:
            a += 1
        else:
            b += 1

    return []




