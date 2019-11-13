"""
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        res_matrix = []
        for i in range(numRows):
            row = []
            for i in range(s):
                row.append("")
            res_matrix.append(row)

        row_idx = col_idx = 0
        vertical = True
        print(1, res_matrix)

        for i, v in enumerate(s):
            print('her', res_matrix, row_idx, col_idx)
            # while len(res_matrix[row_idx]) <= col_idx:
            #     res_matrix[row_idx].append("")
            res_matrix[row_idx][col_idx] = s[i]

            if vertical:
                if row_idx < numRows - 1:
                    row_idx += 1
                    if row_idx == numRows - 1:
                        vertical = False
            else:
                if row_idx >= 0:
                    col_idx += 1
                    row_idx -= 1
                    if row_idx == 0:
                        vertical = True

        res = ""
        for row in res_matrix:
            sum = ''.join(row)
            res += sum

        return res

s = Solution()
test = s.convert("AB", 1)

print(test)
















