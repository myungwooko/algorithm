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


** if it's hard to explain, it is hard to code <= 맞는 말이다.
** don't fixate to that complex one
** find out another approach
** 간단하게 고치면 되는 것들을 오늘 왜 그랬을까, 영어도 그렇고 => 더 많이 연습할 것, pramp + a
'''


def availableTime(times):
    candidates = []
    for time in times:
        candidates += time

    times = sorted(candidates, key=lambda x: x[0])

    idx = 0
    res = []
    while idx < len(times) - 1:
        if times[idx][1] > times[idx + 1][0] or times[idx][1] > times[idx + 1][1]:
            times[idx] = (min(times[idx][0], times[idx + 1][0]), max(times[idx][1], times[idx + 1][1]))
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











