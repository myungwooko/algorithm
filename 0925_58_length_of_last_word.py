"""
58. Length of Last Word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

이런 케이스에 대한 질문과 생각을 했으면 더 좋았을텐데! => "a " or " "
문제 파악에 더 신경쓰다.
Concentrate to what the problem's intention is more.
"""
class Solution:
    def lengthOfLastWord(self, s) -> int:
        if not s.strip():
            return 0
        str_list = s.split()
        return len(str_list[-1])


s = Solution()
test1 = s.lengthOfLastWord("Hello World")
print(test1)

s = Solution()
test1 = s.lengthOfLastWord("Hello World")
print(test1)

test2 = s.lengthOfLastWord("a ")
print("it should be 1 and yours is ", test2)

""