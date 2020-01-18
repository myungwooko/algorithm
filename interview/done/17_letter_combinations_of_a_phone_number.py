"""
17. Letter Combinations of a Phone Number
Medium

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
""""""""""""""""""""""""""""""""""""""""""""""
리컬젼시에 혹은 변수를 참조하는 경우에서 굉장히 중요한 point

1. res += char -> X
이렇게 하게되면 여기서 아예 바뀌어버리니깐 뒤에도 영향을 주게 된다. 
왜냐면 res 라는 것은 현재 하나의 이름으로 모든 곳에서 다 참조를 하는 것인데 그렇게 아예 변수의 값을 변경해 버리면 그것으로 정해져 버리기 때문에 문제가 생긴다.
이러한 경우에서는.

2. helper(digits, idx+1, res+char) -> O
res+char를 argument(인수)로서 넣는것은 선언하는 것과 아무런 상관이 없는 것. 그냥 그값을 넣는 것일뿐이다. 그러므로 이 경우에 참조되는 값은 아무런 영향을
받지 않는다.  
"""

def letterCombinations(digits):
    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []

    def helper(digits, idx, res):
        if len(res) == len(digits):
            result.append(res)
            return
        for char in dic[digits[idx]]:
            res += char
            helper(digits, idx + 1, res)

    helper(digits, 0, "")
    return result


def letterCombinations(digits):
    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []

    def helper(digits, idx, res):
        if len(res) == len(digits):
            result.append(res)
            return
        for char in dic[digits[idx]]:
            helper(digits, idx + 1, res + char)

    helper(digits, 0, "")
    return result


num = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


test = letterCombinations(num)
print(test)
