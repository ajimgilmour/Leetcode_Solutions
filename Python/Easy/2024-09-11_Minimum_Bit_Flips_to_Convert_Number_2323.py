# Problem: Minimum Bit Flips to Convert Number
# Question ID: 2323
# Difficulty: Easy
# Solved Date: 2024-09-11
# LeetCode URL: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

// https://leetcode.com/problems/minimum-bit-flips-to-convert-number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_value = start ^ goal
        return bin(xor_value).count('1')
        
