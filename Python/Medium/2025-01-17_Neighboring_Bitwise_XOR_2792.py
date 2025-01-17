# Problem: Neighboring Bitwise XOR
# Question ID: 2792
# Difficulty: Medium
# Solved Date: 2025-01-17
# LeetCode URL: https://leetcode.com/problems/neighboring-bitwise-xor/

// https://leetcode.com/problems/neighboring-bitwise-xor

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
