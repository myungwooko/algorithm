"""
28. strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an _interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().



*문제를 풀기전 해야하는 질문:
    - 만약 needle이 "" 이라면?


* 참고 using 1 for loop
    - a[0:0]            => ''
    - a == b == 0       => 다중 가능
"""


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for idx in range(len(haystack)):
        if haystack[idx] == needle[0] and len(haystack[idx:]) >= len(needle):
            count = 0
            for i in range(0, len(needle)):
                if haystack[idx + i] != needle[i]:
                    break
                else:
                    count += 1
                    if count == len(needle):
                        return idx
    return -1


"""
참고풀이
"""


def strStr(haystack, needle):
    if haystack == needle == '':
        return 0

    n = len(needle)

    for i in range(
            len(haystack) - n + 1
    ):  # 해당 계산은 => "만약 중간에 나오지 않았다면 유효 검사 대상의 앞글자가 되는 자신부터 끝날때까지의 길이가 needle의 길이인 것까지는 검사를 해봐야 알수 있는 거니까. 이 이상은 길이가 넘어가는 거므로 표현을 못하니 할필요없고" 에서 나온것.
        if haystack[i:i + n] == needle:
            return i

    return -1


print(strStr("hello", ""))
