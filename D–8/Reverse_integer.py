"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
 Input: x = 123
 Output: 321

Example 2:
 Input: x = -123
 Output: -321

Example 3:
 Input: x = 120
 Output: 21
"""

class Solution:
    def reverse(self, x):
        
#        flag = True if x < 0 else False
#       if flag:
#           x = -x
#       x = str(x)[::-1]

#       if flag:
#           x = "-" + x

#       value = 2 ** 31
#       x = int(x)
#       if -value <= x < value:
#           return x
#       return 0
        
        is_neg = False
        if x < 0:
            x = -x
            is_neg = True

        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x //= 10
        if is_neg:
            res = -res

        if res < -2**31 or res > 2**31-1:
            return 0
        return res