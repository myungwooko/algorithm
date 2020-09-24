"""
168. Excel Sheet Column Title
Easy

Share
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

additional information
MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words,
column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.

Given a column number, find its corresponding Excel column name. Following are more examples.

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC

alphabet 26개 -> ... 26X26X26(ABC) 26X2(AB) 26(A)


- 자리수 => 26^1까지는 한자리, 26^2( + 26 **)까지는 두자리, 26^3(+ 그전까지의 누적)까지는 세자리...
==> pow의 계산은 그 자리수가 만들어내는 모든 경우의 수일 뿐이고 총 개수는 그 전까지의 누적을 다 더해야 맞다. 예를들면, ZZ 까지의 모든 경우의 수는 26x26(두자리의 모든 경우의 수) + 26(한자리의 경우의 수)
- 각위치의 것들이 무엇인지는 ABC 세자리이면 3번쨰 자리는 26^2가 몇개이냐(ex 4개면 3번쨰 자리는 D), 2번째 자리는 26^1이 몇개이냐(ex 2개면 2번쨰자리는 B), 1번쨰 자리는 나머지 개수 맞춰서.
==> 다만 26으로 딱 나누어 떨어지면 그때는 나온 몫의 -1 개수 왜냐면  26이 Z이고 52 AZ이니까 나머지가 생길때부터 유효한 것.

=> 패턴을 보니 그런것 같다.
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string

        alphabet = string.ascii_uppercase
        exponent = 1
        acc = 0
        while True:
            acc += pow(26, exponent)
            if n > acc:
                exponent += 1
            else:
                break

        result_list = []
        exponent -= 1

        while exponent:
            d, m = divmod(n, pow(26, exponent))
            if m == 0:
                d -= 1  # 52=AZ니까
            result_list.append(alphabet[d - 1])
            n = m
            exponent -= 1

        result_list.append(alphabet[n - 1])

        return "".join(result_list)


s = Solution()
test = s.convertToTitle(701)
print(1, test)
