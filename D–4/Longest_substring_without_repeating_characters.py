"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
 Input: s = "abcabcbb"
 Output: 3
 Explanation: The answer is "abc", with the length of 3.

Example 2:
 Input: s = "bbbbb"
 Output: 1
 Explanation: The answer is "b", with the length of 1.

Example 3:
 Input: s = "pwwkew"
 Output: 3
 Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     sls = len(set(s))
    #     ls = len(s)
    #     if ls >= 1:
    #         max_l = 1
    #     else:
    #         return 0
    #     for i in range(ls):
    #         for j in range(i + max_l + 1, i + sls + 1):
    #             curr = s[i:j]
    #             c_ls = len(curr)
    #             if len(set(curr)) != c_ls:
    #                 break
    #             else:
    #                 if c_ls > max_l:
    #                     max_l = c_ls
    #                     if max_l == sls:
    #                         return sls
    #     return max_l

    # def lengthOfLongestSubstring(self, s):
    #     sls = len(set(s))
    #     ls = len(s)
    #     if ls >= 1:
    #         max_l = 1
    #     else:
    #         return 0
    #     for i in range(ls):
    #         for j in reversed(range(i + max_l + 1, i + sls + 1)):
    #             curr = s[i:j]
    #             c_ls = len(curr)
    #             if len(set(curr)) == c_ls:
    #                 if c_ls > max_l:
    #                     max_l = c_ls
    #                     if max_l == sls:
    #                         return sls
    #                 break
    #     return max_l

    # def lengthOfLongestSubstring(self, s):
    #     exist = [False] * 256
    #     ls = len(s)
    #     max_len = i = 0
    #     for j in range(ls):
    #         while(exist[ord(s[j])]):
    #             exist[ord(s[i])] = False
    #             i += 1
    #         exist[ord(s[j)] = True
    #         max_len = max(max_len, j - i + 1)
    #     return max_len

    def lengthOfLongestSubstring(self, s):
        
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i
            
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len