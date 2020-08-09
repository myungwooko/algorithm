# """
# gingerbrave
# gingerbright
# gumball	soda
# salt
# strawberry
# beet
# blackberry
#
# """
#
#
# def solution(names):
#     answer = 0
#     room1 = []
#     room2 = []
#
#     for name in names:
#
#         count1 = 0
#         for n1 in room1:
#             if name[0] == n1[0]:
#                 count1 += 1
#
#         if count1 == 0:
#             room1.append(name)
#             continue
#
#         count2 = 0
#         for n2 in room2:
#             if name[0] == n2[0]:
#                 count2 += 1
#
#         if count1 < count2:
#             room1.append(name)
#         else:
#             room2.append(name)
#
#     p1 = 0
#     for i in range(len(room1)):
#         for j in range(i + 1, len(room1)):
#             if room1[i][0] == room1[j][0]:
#                 p1 += 1
#
#     p2 = 0
#     for i in range(len(room2)):
#         for j in range(i + 1, len(room2)):
#             if room2[i][0] == room2[j][0]:
#                 p2 += 1
#
#     answer = p1 + p2
#
#     return answer
#
#
#
#
#
# """
#
# 예티들은 원하는 크기의 눈덩이를 만들 수 있으며,
# 아이스크림 협곡의 정해진 위치에서 오른쪽 혹은 왼쪽 방향으로만 던질 수 있다.
# 던져진 눈덩이들은 모두 같은 속력으로 이동하고,
# 눈덩이들끼리 충돌하면 작은 눈덩이는 곧바로 바닥에 떨어지지만 큰 눈덩이는 그대로 날아간다.
# 만약 크기가 같은 눈덩이들이 충돌하면 둘 모두 바닥에 떨어지게 된다.
# 따라서 눈덩이들이 현란하게 날아다니는 것에 비해
# 용감한 쿠키가 실제로 신경써야 하는 눈덩이는 많지 않을 수 있다.
# """
# """
# - 다음 list 만들기
# - 다음 element와 부호가 같으면 자신은 다음멤버로 간다.
# - 부호가 다르면 현재 index와 다음 index의 값을 비교 큰것만 다음멤버로 간다. 그리고 index
# """
#
# def solution(snowballs):
#     answer = []
#     for ball in snowballs:
#         answer.append(ball)
#         while len(answer) >= 2 and answer[-2] > 0 and answer[-1] < 0:
#             x = answer.pop()
#             y = answer.pop()
#             if abs(x) > abs(y):
#                 answer.append(x)
#             elif abs(x) < abs(y):
#                 answer.append(y)
#     return answer
#
#
# def solution(K, A):
#     answer = [0]
#
#     def helper(curr_num, rest):
#         if not rest:
#             return
#         answer[0] += 1
#
#         print("count:", answer[0], "rest", rest)
#
#         idx = 0
#         while idx < len(rest):
#             if rest[idx] == curr_num + 1:
#                 rest.pop(idx)
#                 curr_num = curr_num + 1
#                 continue
#             idx += 1
#
#         if len(rest) > 1:
#             helper(rest[0], rest[1:])
#         elif len(rest) == 1:
#             answer[0] += 1
#         else:
#             return
#
#     helper(A[0], A[1:])
#     return answer[0]
#
#
# # def solution(K, A):
# #     answer = [0]
# #
# #     queue = [(A[0], A[1:])]
# #
# #     while queue:
# #         curr_num, rest = queue.pop(0)
# #         if not rest:
# #             break
# #         answer[0] += 1
# #
# #         idx = 0
# #         while idx < len(rest):
# #             if rest[idx] == curr_num + 1:
# #                 rest.pop(idx)
# #                 curr_num = curr_num + 1
# #                 continue
# #             idx += 1
# #
# #         if len(rest) > 1:
# #             queue.append((rest[0], rest[1:]))
# #         elif len(rest) == 1:
# #             answer[0] += 1
# #         else:
# #             break
# #
# #     return answer[0]
#
#
# # seen
# def solution(K, A):
#     answer = 0
#     seen = set()
#     for n in A:
#         if len(seen) == 0 or n - 1 not in seen:
#             seen.add(n)
#             answer += 1
#         else:
#             seen.add(n)
#     return answer
#
#
# k, input = 5, [1, 3, 4, 2, 5]
# k, input = 10, [2, 2, 2, 1, 4]
# k, input = 10, [5, 6, 7, 8, 9]
# # test = solution(k, input)
# # print(test)
#
#
#
# import math
# """
# - instance가 있다
# - second마다 만나는 수가 index순으로 나열
# - num < 25         => instance가 1보다 크면 반으로 줄인다. (ceiling)
# -                  => instance가 1이면 no action
# - 25 <= num <= 60  =>  no action
# - num > 60         =>  insance * 2 , if that is smaller than 2*10^8
#
# - 더해지거나 빼는 연산을 하면 10초를 쉰다 idx 10개를 넘어간다는 말
# """
#
# def finalInstances(instances, averageUtil):
#     # Write your code here
#     i = 0
#     while i < len(averageUtil):
#         val = averageUtil[i]
#         print("i, val", i, val)
#         if val < 25:
#             if instances > 1:
#                 instances = math.ceil(instances/2)
#                 i += 11
#                 if i >= len(averageUtil):
#                     break
#                 continue
#         elif val > 60:
#             print("22, val, instances", val, instances, instances*2)
#             if instances*2 <= (2*(pow(10, 8))):
#                 print("33, val, instances", val, instances)
#                 instances *= 2
#                 i += 11
#                 if i >= len(averageUtil):
#                     break
#                 print(averageUtil[i])
#                 print("i", i)
#                 continue
#         i += 1
#     return instances
#
#
# # instances = 2
# # ave = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
# # ave = [1, 3, 5, 10, 80]
#
# instances = 13
# ave = [40, 89, 79, 76, 66, 60, 8, 90, 19, 39, 53, 30, 93]
#            # 26
# test = finalInstances(instances, ave)
# print(test)
#
#
# """
# fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvumnwehj
# hnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqs
# imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypstsxhp
# rrmbeddvphnegtuxxtalsyxezjwtlwmxvrjtxytykkckuvbhhlovgcxjxhhivxnutkxvhadiaysulvknmcanhsyxlivarjdk
# spwvpfyfpkvgthqqrmajxispjncxgviyuqavayvsvznmhskodmidajwlkf
#
#
#
# fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvumnwehj
# hnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqs
# imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypstsxhp
# oswnprlhvsuzvgyeettenngipfvrflpprjjalchhhcmhxkupciulccqssaqgdttpldmzdzveslyjadswtsbhgkddeouxbldsxzmfvhtonlampljgzyvem
# rrmbeddvphnegtuxxtalsyxezjwtlwmxvrjtxytykkckuvbhhlovgcxjxhhivxnutkxvhadiaysulvknmcanhsyxlivarjdk
# spwvpfyfpkvgthqqrmajxispjncxgviyuqavayvsvznmhskodmidajwlkf
#
#
# """
#
#
#
#

