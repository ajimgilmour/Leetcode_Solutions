# Problem: Minimum Common Value
# Question ID: 2634
# Difficulty: Easy
# Solved Date: 2025-03-14
# LeetCode URL: https://leetcode.com/problems/minimum-common-value/

// https://leetcode.com/problems/minimum-common-value

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1]<nums2[0] or nums2[-1]<nums1[0]:
            return -1
            
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
