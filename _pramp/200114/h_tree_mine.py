import math

print
"Practice makes Perfect!"


# there is center (x, y), depth = 1
# recursive
def drawLine(p1, p2):
    print("{}->{}".format(p1, p2))


def hTree(x, y, length, depth):
    if depth == 0:
        return
    length = length / 2
    up = y + length
    down = y - length
    right = x + length
    left = x - length
    y_center = y
    next_length = length / math.sqrt(2)
    next_depth = depth - 1

    drawLine((left, down), (left, up))
    drawLine((left, y_center), (right, y_center))
    drawLine((right, down), (right, up))

    hTree(left, down, next_length, next_depth)
    hTree(left, y_center, next_length, next_depth)
    hTree(left, up, next_length, next_depth)
    hTree(right, down, next_length, next_depth)
    hTree(right, y_center, next_length, next_depth)
    hTree(right, up, next_length, next_depth)


hTree(0, 0, 8, 5)
