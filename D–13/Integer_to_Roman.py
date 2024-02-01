"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
 Input: num = 3
 Output: "III"
 Explanation: 3 is represented as 3 ones.

Example 2:
 Input: num = 58
 Output: "LVIII"
 Explanation: L = 50, V = 5, III = 3.

Example 3:
 Input: num = 1994
 Output: "MCMXCIV"
 Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# class Solution(object):
#         def intToRoman(self, num: int) -> str:
#         """
#         :type num: int
#         :rtype: str
#         """
#
class Solution(object):
    # def intToRoman(self, num: int) -> str:
        ## http://www.rapidtables.com/convert/number/how-number-to-roman-numerals.htm
        # roman_dim = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        #             [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
        #             [9,'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        # if num == 0:
        #     return ''
        # roman_str = ''
        # current, dim = num, 0
        # while current != 0:
        #     while current // roman_dim[dim][0] == 0:
        #         dim += 1
        #     while current - roman_dim[dim][0] >= 0:
        #         current -= roman_dim[dim][0]
        #         roman_str += roman_dim[dim][1]
        # return roman_str

    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV",
                   "I"]
        roman = ''
        i = 0
        while num > 0:
            k = num // values[i]
            for j in range(k):
                roman += symbols[i]
                num -= values[i]
            i += 1
        return roman

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.intToRoman(90)