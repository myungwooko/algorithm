"""
22. Generate Parentheses
Medium

3908

218

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    # brute force 다 만들고 검사
    def generateParenthesis(self, n: int):
        """
        - 모든 가능한것들을 만들어보고
        - 밸런스 검사기를 돌려서 남은것들의 집합을 리턴?
        """
        results = []

        def helper(acc):
            if len(acc) == n * 2:
                results.append(acc)
                return
            candidates = ["(", ")"]
            for i in candidates:
                helper(acc + i)
            return

        helper("(")
        return [i for i in results if self.validParenthesis(i)]

    def validParenthesis(self, s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == "(":
                        stack.pop()
        if not stack:
            return True
        return False

    # 검사도 동시에 하면서 빠르게 조건 선별 가능후보만 진행 => 하지만 위와 크게 차이나는 건 아니다.
    def generateParenthesis(self, n):
        self.res = []
        self.dfs(n, n, "")
        return self.res

    def dfs(self, leftremains, rightremains, path):
        # leftremains > rightremains means 열거는 있는데 그걸 닫을게 없다는 의미. have elements to open but doesn't have elements to close that opened
        if leftremains > rightremains or leftremains < 0 or rightremains < 0:
            return
        if leftremains == 0 and rightremains == 0:
            self.res.append(path)
            return
        self.dfs(leftremains - 1, rightremains, path + "(")
        self.dfs(leftremains, rightremains - 1, path + ")")

s = Solution()
test = s.generateParenthesis(3)
print(test)