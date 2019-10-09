"""
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

"""
조합으로 만드는게 아니라 말 그대로 반대인 문제였음

list.revserse() => None을 return => 행위로 '바라보는곳'을 바꿔줄뿐 행위 자체는 아무것도 리턴하지 않는다.

"""
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    rev = [e for e in str(x)]
    rev.reverse()
    rev = int("".join(rev))
    if rev == x:
        return True
    else:
        return False


print(isPalindrome(100))