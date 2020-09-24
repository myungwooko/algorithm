"""
856. Score of Parentheses
Medium

Share
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:
S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


class Solution:
    def scoreOfParentheses(self, S):
        # 결과 값 저장을 한칸 앞에다 해주면서 나가는 식이라서 이런 것 같다.
        stack = [0]
        for i in S:
            if i == "(":
                # 각각의 순서를 유효하게 count해주는 느낌.
                stack.append(0)
            else:
                # 해당 순서가 ")"이니까 pop된 것과 함께 완결이 되는 ()를 하나 만들어준다고 생각하면 된다.
                last = stack.pop()
                # 이전까지 쌓인게 없는것이라면(0) 독립적인 하나로서 1이 되는 거고, 쌓인게 있었다면 그것의 2배가 되는 것을 물고가도록 두배를 계산해서 넘겨준다.
                # 앞에 저장 시키는 이유는 앞에서 더할건 더하며 물고가다가 해당의 뒤(")")를 만나면 그때 x2를 계산해주는 느낌.
                # 두배가 된것으로서 유효한거면 거기서 또 두배를 시켜주고, 만약 그게 아니었다면 => 하나의 독립적인 것으로서 생성된 것이므로 1을 더해줘서 물고가게 해준다. 나중에 자신 곱하기 2할때 2배가 되니깐.
                stack[-1] += last * 2 or 1
        return stack[-1]


S = "(()(()))"
s = Solution()
test = s.scoreOfParentheses(S)
print(test)
