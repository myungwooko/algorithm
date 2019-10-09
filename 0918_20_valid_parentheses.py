"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


solution => stack 이용 => 어쨌든 다 간단하게들 푸는군 생각을 해보자. 문제를 잘 파악하고, "잘" 풀도록 하자.
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack or {')':'(',']':'[','}':'{'}[i]!=stack[-1]:
                    return False
                stack.pop()
        return not stack


s = Solution()
test_1 = s.isValid("{{()}}")
print(test_1)

test_2 = s.isValid("()[]{}")
print(test_2)

test_3 = s.isValid(("["))
print(test_3)


