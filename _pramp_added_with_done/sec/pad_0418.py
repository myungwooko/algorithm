# def count(n1, n2):
#     nums = list(range(10))
#     print(nums)
#     count = countR = 0
#     n1, n2 = int(n1), int(n2)
#
#     idx = n1
#     while idx != n2:
#         count += 1
#         if idx == len(nums) - 1:
#             idx = 0
#         else:
#             idx += 1
#
#     idx = n1
#     while idx != n2:
#         countR += 1
#         if idx == 0:
#             idx = len(nums) - 1
#         else:
#             idx -= 1
#     print("count, countR", count, countR)
#     return min(count, countR)
#
#
# def solution(p, s):
#     res = 0
#     for i in range(len(p)):
#         res += count(p[i], s[i])
#     return res

#
# p = "82195"
# s = "64723"
#
# print(solution(p, s))
"""
- 물건 -1
- 먼지의 양은 0이상의 정수
- go => 바라보고 있는 방향으로 한칸 전진, 범위밖 or 물건 x
- left => 왼쪽으로 회전
- right => 오른쪽으로 회전

- 먼지의 양이 0이어도 방문은 하지만 청소 먼지의 량은 0


- r, c 북쪽을 바라보고 시작 r => row, c => column
- move 수행 방향 배열(만약 현재 위치에서 수행방향으로 이동이 불가한 경우 그 방향은 지나가게 되고 다음 방향 수행으로 넘어감.)
- output(int): 방향이 주어진 배열대로 청소를 수행한다고 했을때 총 청소한 먼지의 양을 return 
- NxN  2 <= N <= 20
- 칸    0 <= 칸 <= 100
"""
"""
- 물건 -1
- 먼지의 양은 0이상의 정수
- go => 바라보고 있는 방향으로 한칸 전진, 범위밖 or 물건 x
- left => 왼쪽으로 회전
- right => 오른쪽으로 회전

- 먼지의 양이 0이어도 방문은 하지만 청소 먼지의 량은 0


- r, c 북쪽을 바라보고 시작 r => row, c => column
- move 수행 방향 배열(만약 현재 위치에서 수행방향으로 이동이 불가한 경우 그 방향은 지나가게 되고 다음 방향 수행으로 넘어감.)
- output(int): 방향이 주어진 배열대로 청소를 수행한다고 했을때 총 청소한 먼지의 양을 return 
- NxN  2 <= N <= 20
- 칸    0 <= 칸 <= 100
"""
"""
- 물건 -1
- 먼지의 양은 0이상의 정수
- go => 바라보고 있는 방향으로 한칸 전진, 범위밖 or 물건 x
- left => 왼쪽으로 회전
- right => 오른쪽으로 회전

- 먼지의 양이 0이어도 방문은 하지만 청소 먼지의 량은 0


- r, c 북쪽을 바라보고 시작 r => row, c => column
- move 수행 방향 배열(만약 현재 위치에서 수행방향으로 이동이 불가한 경우 그 방향은 지나가게 되고 다음 방향 수행으로 넘어감.)
- output(int): 방향이 주어진 배열대로 청소를 수행한다고 했을때 총 청소한 먼지의 양을 return 
- NxN  2 <= N <= 20
- 칸    0 <= 칸 <= 100
"""


def solution(office, r, c, move):
    answer = []

    def helper(r, c, direction, move_idx, answer):
        print(answer)
        if move_idx == len(move):
            return

        if move[move_idx] == "go":
            if direction == "north":
                if r - 1 >= 0 and office[r - 1][c] != -1:
                    answer.append(office[r - 1][c])
                    office[r - 1][c] = 0
                    r -= 1
                helper(r, c, direction, move_idx + 1, answer)
            elif direction == "south":
                if r + 1 < len(office) and office[r + 1][c] != -1:
                    answer.append(office[r + 1][c])
                    office[r + 1][c] = 0
                    r += 1
                helper(r, c, direction, move_idx + 1, answer)
            elif direction == "west":
                if c - 1 >= 0 and office[r][c - 1] != -1:
                    answer.append(office[r][c - 1])
                    office[r][c - 1] = 0
                    c -= 1
                helper(r, c, direction, move_idx + 1, answer)
            elif direction == "east":
                if c + 1 < len(office[0]) and office[r][c + 1] != -1:
                    answer.append(office[r][c + 1])
                    office[r][c + 1] = 0
                    c += 1
                helper(r, c, direction, move_idx + 1, answer)

        elif move[move_idx] == "right":
            if direction == "north":
                direction = "east"
            elif direction == "east":
                direction = "south"
            elif direction == "south":
                direction = "west"
            elif direction == "west":
                direction = "north"
            helper(r, c, direction, move_idx + 1, answer)
        elif move[move_idx] == "left":
            if direction == "north":
                direction = "west"
            elif direction == "west":
                direction = "south"
            elif direction == "south":
                direction = "east"
            elif direction == "east":
                direction = "north"
            helper(r, c, direction, move_idx + 1, answer)

        return

    answer += [office[r][c]]
    office[r][c] = 0
    helper(r, c, "north", 0, answer)
    return sum(answer)


#
#
office = [[-1, -1, 4], [6, 3, -1], [2, -1, 1]]
r, c = 1, 0
move = ["go", "go", "right", "go", "right", "go", "left", "go"]

test = solution(office, r, c, move)
print(test)

#
#
# def solution(numbers, K):
#     answer = []
#
#     queue = [numbers]
#     seen = []
#     count = 0
#     seen.append(numbers)
#
#     while queue:
#         curr_nums = queue.pop(0)
#         flag = True
#         for k in range(1, len(curr_nums)):
#             if curr_nums[k] - curr_nums[k - 1] > K:
#                 flag = False
#
#         if flag:
#             return count
#
#         for i in range(len(curr_nums) - 1):
#             for j in range(i + 1, len(curr_nums)):
#                 curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]
#                 if curr_nums not in seen:
#                     queue.append(curr_nums)
#                     seen.append(curr_nums)
#                     count += 1
#                 curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]
#
#     return -1
#
#
# numbers, K = [10, 40, 30, 20], 20
# test = solution(numbers, K)
# print(test)
#
#
#
#
#
#
#
