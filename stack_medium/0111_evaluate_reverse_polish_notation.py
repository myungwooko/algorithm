"""
150. Evaluate Reverse Polish Notation
Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
import math


class Solution(object):
    #and this is for python3
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        """
        - Division between two integers should truncate toward zero.=> truncate after point
        - The given RPN expression is always valid. That means the expression would always evaluate 
        to a result and there won't be any divide by zero operation. => operater follows two operands.

        algorithms  
        - when meet an operator, 오퍼레이터 앞 두 operands를 해당 오퍼레이터를 통해서 연산한다. 
        - 해당 오퍼레이터 인덱스에 그 결과를 넣는다. 
        - 해당 오퍼레이터 인데스 - 2 위치를 두번 삭제한다. 
        - while 1 < len(tokens)
        * 나눗셈 연산 => 0으로 가깝게 => 음수면 올림, 양수면 내림. 
        - 언제나 유효 => 만약 딱 하나의 결과가 나오지 않으면 마지막 값을 리턴
        """
        operators = ["+", "-", "*", "/"]
        for i, v in enumerate(tokens):
            if v not in operators:
                tokens[i] = int(v)

        def helper(idx):
            operator = tokens[idx]
            if operator == '+':
                v = tokens[idx - 2] + tokens[idx - 1]
                tokens[idx] = v
            elif operator == '-':
                v = tokens[idx - 2] - tokens[idx - 1]
                tokens[idx] = v
            elif operator == '*':
                v = tokens[idx - 2] * tokens[idx - 1]
                tokens[idx] = v
            else:
                r = float(tokens[idx - 2] / tokens[idx - 1])
                print(tokens[idx - 2], tokens[idx - 1], r)
                if r < 0:
                    c = math.ceil(r)
                else:
                    c = math.floor(r)
                tokens[idx] = int(c)
            for _ in range(2):
                del tokens[idx - 2]

        idx = 0
        while 1 < len(tokens) and idx < len(tokens):
            if tokens[idx] in operators:
                print(1, "//", idx, "//", tokens)
                helper(idx)
                print(2, tokens)
                idx -= 2
            idx += 1
            print(3, idx)
        return tokens[-1]

    #and this is for python2
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if l * r < 0 and l % r != 0:
                        stack.append(l / r + 1)
                    else:
                        stack.append(l / r)
        return stack.pop()


tokens = [
    "3", "-19", "-", "13", "33", "+", "-", "-1", "-", "3", "34", "+", "21",
    "+", "-", "39", "+", "-6", "16", "14", "-", "-", "/", "-20", "+", "-5",
    "-", "2", "-", "32", "-", "10", "+", "30", "-", "2", "+", "29", "+", "-4",
    "-2", "+", "+", "-13", "+", "26", "-", "11", "+", "16", "-10", "+", "-",
    "-19", "+", "-5", "+", "21", "-13", "+", "-", "31", "+", "24", "+", "37",
    "-", "10", "-", "34", "-", "-10", "+", "-12", "-", "17", "+", "-1", "+",
    "38", "-", "11", "31", "30", "+", "+", "+", "3", "+", "5", "+", "36", "-",
    "7", "-", "8", "+", "1", "26", "-7", "+", "-", "-", "-4", "-", "-20", "-",
    "-10", "19", "+", "+", "24", "-", "24", "-", "-12", "-10", "+", "+", "-10",
    "-", "-16", "+", "38", "+", "22", "-7", "+", "+", "28", "+", "19", "-",
    "17", "-7", "*", "-9", "-", "+", "-18", "+", "10", "-", "20", "+", "-13",
    "+", "4", "-6", "-", "+", "3", "-", "28", "25", "+", "-17", "4"
]
s = Solution()
test = s.evalRPN(tokens)
print(test)
