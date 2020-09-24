"""
passwordTime

passwordTime(password, keypad) => return the seconds how long it will take,
- from password start to password end
- one step takes one second
- but same point takes 0 second

keyPad = "0123456789abcdef"
password = "567bbe"

passwordTiem(password, keyPad) will return 4
"""


def passwordTime(password, keyPad):
    keyPad = [
        list(keyPad[:4]),
        list(keyPad[4:8]),
        list(keyPad[8:12]),
        list(keyPad[12:16])
    ]
    m = len(keyPad)
    n = len(keyPad[0])
    for i in range(m):
        for j in range(n):
            if keyPad[i][j] == password[0]:
                firstPoint = (i, j, 1, 0)

    queue = [firstPoint]

    while queue:
        x, y, idx, count = queue.pop(0)
        if idx == len(password):
            return count

        if keyPad[x][y] == password[idx]:
            queue.append((x, y, idx + 1, count))
            continue
        candidates = [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                      (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1)]
        for x1, y1 in candidates:
            if 0 <= x1 < m and 0 <= y1 < n:
                #여기서 해당 처리를 해줬어야 했다.
                if keyPad[x1][y1] == password[idx]:
                    queue.append((x1, y1, idx + 1, count + 1))
                else:
                    queue.append((x1, y1, idx, count + 1))
    return


keyPad = "0123456789abcdef"
# password = "16bcd83"
password = "16b"
test = passwordTime(password, keyPad)
print(test)
