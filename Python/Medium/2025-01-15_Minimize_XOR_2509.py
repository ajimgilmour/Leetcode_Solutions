# Problem: Minimize XOR
# Question ID: 2509
# Difficulty: Medium
# Solved Date: 2025-01-15
# LeetCode URL: https://leetcode.com/problems/minimize-xor/

// https://leetcode.com/problems/minimize-xor

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
        return res
