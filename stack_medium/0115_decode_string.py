"""
394. Decode String

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str



        - s의 li는 그대로 두므로 인덱스 걱정은 할 필요 없는거고,
        - li를 다 도는 동안만 하면 된다.
        - stack은 계산 해나가며 쌓아간다.
        - bracket의 짝이 만들어지면 stack안에 쌓인것을 통해 num과 chars를 구해서 계산 stack에 쌓아나간다. => li를 다 돌때까지 반
        """
        li = list(s)
        bracket = ["[", "]"]
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        stack = []
        bracketStack = []
        for i in li:
            stack.append(i)
            if i in bracket:
                bracketStack.append(i)
            num = ""
            chars = ""
            if bracketStack[-2:] == ["[", "]"]:
                stack.pop()
                bracketStack.pop()
                bracketStack.pop()
                while stack[-1] != "[":
                    chars = stack.pop() + chars
                stack.pop()
                while stack and stack[-1] in nums:
                    num = stack.pop() + num
                product = int(num)*chars
                stack.append(product)
        return ''.join(stack)


input1 = "3[a]2[bc]"
input2 = "100[lele]"
s = Solution()
test = s.decodeString(input2)
print(test)





















