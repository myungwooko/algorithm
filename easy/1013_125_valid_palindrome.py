"""
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

- 그렇지 palindrom은 결국 거꾸로 해도 똑같은거지 => 거꾸로해도 이효리
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alnum = [i.lower() for i in s if i.isalnum()]
        return only_alnum == only_alnum[::-1]

    def isPalindrome1(self, s):
        s = ''.join(
            e for e in s
            if e.isalnum()).lower()  # (안에 넣으니까 list로 인식하고 그렇게 때문에 가능한가 보다.)
        return s == s[::-1]


s = Solution()
test1 = s.isPalindrome("A man, a plan, a canal: Panama")
test2 = s.isPalindrome("race a car")
print(test1, True)
print(test2, False)
