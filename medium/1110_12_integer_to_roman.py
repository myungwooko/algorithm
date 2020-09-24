"""
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if type(num) != int:
            return

        the_num = int(num)
        if the_num < 1 or 3999 < the_num:
            return

        base = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        inv_base = {v: k for k, v in base.items()}

        divider = [1000, 100, 10, 1]
        res_nums = []

        for d in divider:
            num = the_num // d
            res_nums.append(num)
            the_num = the_num % d

        print(res_nums)

        power = 3
        res = ""
        for res_num in res_nums:
            print(res_num)
            if res_num == 0:
                power -= 1
                continue
            powered = pow(10, power)
            power -= 1
            if res_num == 4 or res_num == 9:
                diff_roman = inv_base[powered]
                actual_num = res_num * powered
                standard = actual_num + powered
                standard_roman = inv_base[standard]
                roman = diff_roman + standard_roman
                res += roman
            else:
                roman = ""
                if res_num >= 5:
                    fived = 5 * powered
                    roman += inv_base[fived]
                    roman += (res_num - 5) * inv_base[powered]
                    res += roman
                else:
                    roman += res_num * inv_base[powered]
                    res += roman

        return res

    def intToRoman1(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
            "I"
        ]
        res = ""
        for n, v in zip(numerals, values):
            res += (num // v) * n
            num %= v
        return res


s = Solution()
content = 300
test = s.intToRoman(content)
print(test)
