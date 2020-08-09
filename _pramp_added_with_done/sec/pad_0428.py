# import sys
#
# class Test1:
#     def add_two_nums(self, num1, num2):
#         num1 = self.str_to_num(num1)
#         num2 = self.str_to_num(num2)
#         sum = num1 + num2
#         print(sum)
#
#     def str_to_num(self, str1):
#         nums_map = {
#             '0': 0,
#             '1': 1,
#             '2': 2,
#             '3': 3,
#             '4': 4,
#             '5': 5,
#             '6': 6,
#             '7': 7,
#             '8': 8,
#             '9': 9
#         }
#
#         position = 1
#         res = 0
#         for i in range(len(str1)-1, -1, -1):
#             curr = nums_map[str1[i]]
#             res += curr*position
#             position *= 10
#
#         return res
#
# try:
#     num1 = sys.argv[1]
#     num2 = sys.argv[2]
#     T1 = Test1()
#     T1.add_two_nums(num1, num2)
# except:
#     print("Please put your minput correctly 1.input has to be two positive integer ex) python test1.py input1 input2")







import sys

class Test2:
    def str_to_num(self, str1):
        nums_map = {
            '일': 1,
            '이': 2,
            '삼': 3,
            '사': 4,
            '오': 5,
            '육': 6,
            '칠': 7,
            '팔': 8,
            '구': 9,
        }

        positions_map = {
            '십': pow(10, 1),
            '백': pow(10, 2),
            '천': pow(10, 3),
            '만': pow(10, 4),
            '억': pow(10, 8),
            '조': pow(10, 12)
        }

        curr = 0
        acc = []
        res = []
        if "억" not in str1 and "조" not in str1 and "만" not in str1:
            flag_10000 = True
        else:
            flag_10000 = False
            before = str1.split("만")[0]
            if "십" not in before and "백" not in before and "천" not in before:
                flag_10000 = True

        for i, c in enumerate(str1):
            if c in nums_map:
                curr += nums_map[c]
                if i == len(str1)-1:
                    acc.append(nums_map[c])
                    res.append(sum(acc))
            else:
                if not curr and flag_10000:
                    res.append(positions_map[c])
                else:
                    if c in ['만', '억', '조']:
                        if curr:
                            acc.append(curr)
                        if not acc:
                            acc.append(curr)
                        res.append(sum(acc)*positions_map[c])
                        acc = []
                        curr = 0
                        if c == "만":
                            flag_10000 = True
                    else:
                        if curr:
                            curr *= positions_map[c]
                        else:
                            curr += positions_map[c]
                        acc.append(curr)
                        if i == len(str1)-1:
                            res.append(sum(acc))
                        curr = 0

        return sum(res)

    def num_to_str(self, num):
        num = str(num)
        nums_map = {
            '1': '일',
            '2': '이',
            '3': '삼',
            '4': '사',
            '5': '오',
            '6': '육',
            '7': '칠',
            '8': '팔',
            '9': '구'
        }

        positions_map = {
            pow(10, 1): '십',
            pow(10, 2): '백',
            pow(10, 3): '천',
            pow(10, 4): '만',
            pow(10, 8): '억',
            pow(10, 12): '조'
        }

        position = 1
        bil = []
        mil = []
        thou = []
        nums = []
        for i in range(len(num) - 1, -1, -1):
            n = num[i]
            if n == '0':
                position *= 10
                continue

            num_word = nums_map[n]
            if position == 1:
                nums.insert(0, num_word)
                position *= 10
            else:
                flag = False
                if position >= pow(10, 12):
                    n, r = divmod(position, pow(10, 12))
                    tail = '조'
                    flag = True
                elif position >= pow(10, 8):
                    n, r = divmod(position, pow(10, 8))
                    tail = '억'
                    flag = True
                elif position >= pow(10, 4):
                    n, r = divmod(position, pow(10, 4))
                    tail = '만'
                    flag = True

                if flag:
                    if n != 1:
                        word = num_word + positions_map[n]
                    else:
                        word = num_word
                    if tail == '조':
                        bil.insert(0, word)
                    elif tail == '억':
                        mil.insert(0, word)
                    elif tail == '만':
                        thou.insert(0, word)
                else:
                    word = num_word + positions_map[position]
                    nums.insert(0, word)
                position *= 10

        all_unit_nums = (bil, mil, thou, nums)
        res = ""
        for idx, nums in enumerate(all_unit_nums):
            if idx == 0 and nums:
                res += "".join(nums) + "조"
            if idx == 1 and nums:
                res += "".join(nums) + "억"
            if idx == 2 and nums:
                res += "".join(nums) + "만"
            if idx == 3 and nums:
                res += "".join(nums)

        print(res)
        return

    def add_two_string_nums(self, str1, str2):
        num1, num2 = self.str_to_num(str1), self.str_to_num(str2)
        sum1 = num1 + num2
        self.num_to_str(sum1)


"""
As a command line program 
"""
# try:
#     str1 = sys.argv[1]
#     str2 = sys.argv[2]
#     T2 = Test2()
#     T2.add_two_string_nums(str1, str2)
# except:
#     print("Please put your minput correctly * input has to be strings represents two positive integer ex) python test2.py input1 input2")



"""
For Test below
"""
T2 = Test2()

data = [
    ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
    ['육십사억삼천십팔만칠천육백구', '사십삼'],
    ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
    ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
    ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
    ['천백십일', '구천오백구십구'],
    ['오억사천', '백십일'],
    ['만오천사백삼십', '십구만삼천오백'],
    ['일조', '삼'],
    ['일억', '만'],
]

for pair in data:
    a, b = pair
    T2.add_two_string_nums(a, b)


## Your program is supposed to print to stdout following:
##
## 오백삼십삼조일억천팔백구십이만사천오백사십팔
## 육십사억삼천십팔만칠천육백오십이
## 천사조이천이백일억오천사십이만칠천이
## 육천사백십조일억삼천오백칠십만사천육백삼십삼
## 백십오억사천이백구십오만칠천육백팔십이
## 만칠백십
## 오억사천백십일
## 이십만팔천구백삼십
## 일조삼
## 일억일만














