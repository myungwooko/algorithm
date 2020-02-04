'''
[
  [
    (2, 3),
    (6, 7)
  ],
  [
    (0, 1),
    (5, 6)
  ],
  [
    (1, 2),
    (6, 7),
    (8, 9)
  ]
]

=> [(3, 5), (7, 8)]
'''


def availableTime(times):
    candidates = []
    for time in times:
        candidates += time

    times = sorted(candidates, key=lambda x: x[0])

    idx = 0
    res = []
    while idx < len(times) - 1:
        if times[idx][1] > times[idx + 1][0]:
            times[idx] = times[idx][0], times[idx][1]
            times.pop(idx + 1)
            continue
        else:
            if times[idx][1] != times[idx + 1][0]:
                res.append((times[idx][1], times[idx + 1][0]))
        idx += 1
    return res


times = [
    [
        (2, 3),
        (6, 7)
    ],
    [
        (0, 1),
        (5, 6)
    ],
    [
        (1, 2),
        (6, 7),
        (8, 9)
    ]
]

test1 = availableTime(times)
print(test1)

times2 = [
    [
        (2, 3),
        (6, 7)
    ],
    [
        (0, 100)
    ],
    [
        (1, 2),
        (6, 7),
        (8, 9)
    ]
]

test2 = availableTime(times2)
print(test2)











