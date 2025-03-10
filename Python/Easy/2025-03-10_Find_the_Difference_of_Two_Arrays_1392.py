# Problem: Find the Difference of Two Arrays
# Question ID: 1392
# Difficulty: Easy
# Solved Date: 2025-03-10
# LeetCode URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/

// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        not_in_1 = set()
        not_in_2 = set()
        d1 = {}
        d2 = {}

        for i in range(len(nums1)):
            d1[nums1[i]] = d1.get(nums1[i], 0) + 1

        for i in range(len(nums2)):
            d2[nums2[i]] = d2.get(nums2[i], 0) + 1

        for i in d1.keys():
            if i not in d2:
                not_in_2.add(i)
        
        for i in d2.keys():
            if i not in d1:
                not_in_1.add(i)
        
        return [list(not_in_2), list(not_in_1)]


