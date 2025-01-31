# Problem: Merge Sorted Array
# Question ID: 88
# Difficulty: Easy
# Solved Date: 2025-01-31
# LeetCode URL: https://leetcode.com/problems/merge-sorted-array/

// https://leetcode.com/problems/merge-sorted-array

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = m - 1, n - 1
        i = m + n - 1
        
        while right >= 0 and i >= 0: 
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1
            i -= 1 

