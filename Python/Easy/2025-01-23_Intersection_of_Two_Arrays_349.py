# Problem: Intersection of Two Arrays
# Question ID: 349
# Difficulty: Easy
# Solved Date: 2025-01-23
# LeetCode URL: https://leetcode.com/problems/intersection-of-two-arrays/

// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        for i in nums2:
            if i in d.keys():
                res.append(i)
        return res
