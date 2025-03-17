# Problem: Single Number
# Question ID: 136
# Difficulty: Easy
# Solved Date: 2025-03-17
# LeetCode URL: https://leetcode.com/problems/single-number/

// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
