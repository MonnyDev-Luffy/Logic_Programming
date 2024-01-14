"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility).

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

Example 3:
 Input: s = "A", numRows = 1
 Output: "A"
"""

class Solution:
    
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     ls = len(s)
    #     if ls <= 1 or numRows == 1:
    #         return s
    #     temp_s = []
    #     for i in range(numRows):
    #         temp_s.append(['']*(ls / 2))
    #     inter = numRows - 1
    #     col, row = 0, 0
    #     for i, ch in enumerate(s):
    #         flag = True
    #         if (i / inter) % 2 == 1:
    #             # print i
    #             flag = False
    #         if flag:
    #             temp_s[row][col] = ch
    #             row += 1
    #         else:
    #             temp_s[row][col] = ch
    #             col += 1
    #             row -= 1
    #     result = ''
    #     for i in range(numRows):
    #         result += ''.join(temp_s[i])
    #     return result
    
  def convert(self, s: str, numRows: int) -> str:
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction

    return ''.join(rows)