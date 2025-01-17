# Problem: Sum of Values at Indices With K Set Bits
# Question ID: 3093
# Difficulty: Easy
# Solved Date: 2025-01-17
# LeetCode URL: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                s += nums[i]
        return s
