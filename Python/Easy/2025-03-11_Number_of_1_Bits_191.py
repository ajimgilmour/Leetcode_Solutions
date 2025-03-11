# Problem: Number of 1 Bits
# Question ID: 191
# Difficulty: Easy
# Solved Date: 2025-03-11
# LeetCode URL: https://leetcode.com/problems/number-of-1-bits/

// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = str(bin(n)[2:])
        return c.count('1')

