"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
 Input: nums1 = [1,3], nums2 = [2]
 Output: 2.00000
 Explanation: merged array = [1,2,3] and median is 2.

Example 2:
 Input: nums1 = [1,2], nums2 = [3,4]
 Output: 2.50000
 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     p1 = p2 = 0
    #     ls1 = len(nums1)
    #     ls2 = len(nums2)
    #     all_nums = []
    #     median = 0.0
    #     while p1 < ls1 and p2 < ls2:
    #         if nums1[p1] < nums2[p2]:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #         else:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     if p1 < ls1:
    #         while p1 < ls1:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #     if p2 < ls2:
    #         while p2 < ls2:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     # print all_nums
    #     if (ls1 + ls2) % 2 == 1:
    #         median = all_nums[(ls1 + ls2) / 2]
    #     else:
    #         median = 1.0 * (all_nums[(ls1 + ls2) / 2] + all_nums[(ls1 + ls2) / 2 - 1]) / 2
    #     return median

from ast import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
      return self.findMedianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
      partition1 = (l + r) // 2
      partition2 = (n1 + n2 + 1) // 2 - partition1
      maxLeft1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
      maxLeft2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]
      minRight1 = 2**31 - 1 if partition1 == n1 else nums1[partition1]
      minRight2 = 2**31 - 1 if partition2 == n2 else nums2[partition2]
      if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
      elif maxLeft1 > minRight2:
        r = partition1 - 1
      else:
        l = partition1 + 1