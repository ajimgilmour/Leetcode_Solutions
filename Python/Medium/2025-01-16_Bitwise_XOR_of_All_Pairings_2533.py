# Problem: Bitwise XOR of All Pairings
# Question ID: 2533
# Difficulty: Medium
# Solved Date: 2025-01-16
# LeetCode URL: https://leetcode.com/problems/bitwise-xor-of-all-pairings/

// https://leetcode.com/problems/bitwise-xor-of-all-pairings

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) % 2 != 0:
            for num in nums1:
                res ^= num
        if len(nums1) % 2 != 0:
            for num in nums2:
                res ^= num
    
        return res
