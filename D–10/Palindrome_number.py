"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
 Input: x = 121
 Output: true
 Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
 Input: x = -121
 Output: false
 Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
 Input: x = 10
 Output: false
 Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (x == x[::-1]):
            return True
        return False             
        
    # def isPalindrome(self, x):
    #     if x < 0:
    #         return False
    #     ls = len(str(x))
    #     tmp = x
    #     for i in range(int(ls/2)):
    #         right = int(tmp % 10)
    #         left = tmp / (10 ** (ls - 2 * i - 1))
    #         left = int(left % 10)
    #         if left != right:
    #             return False
    #         tmp = tmp // 10
    #     return True
    
    # def isPalindrome(self, x):
    #     #leetcode book
    #     if x < 0:
    #         return False
    #     div = 1
    #     while x / div >= 10:
    #         div *= 10
    #     while x != 0:
    #         left = x / div
    #         right = x % 10
    #         if left != right:
    #             return False
    #         x = (x % div) / 10
    #         div /= 100
    #     return True

    # def isPalindrome(self, x):
    #     # reverse number
    #     if x < 0:
    #         return False
    #     rev_x = 0
    #     temp = x
    #     while temp != 0:
    #         curr = temp % 10
    #         rev_x = rev_x * 10 + curr
    #         temp = temp // 10
    #     if rev_x == x:
    #         return True
    #     else:
    #         return False

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isPalindrome(1001)