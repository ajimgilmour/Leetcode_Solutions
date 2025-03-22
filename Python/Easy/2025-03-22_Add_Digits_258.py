# Problem: Add Digits
# Question ID: 258
# Difficulty: Easy
# Solved Date: 2025-03-22
# LeetCode URL: https://leetcode.com/problems/add-digits/

// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0 and num != 0:
            return 9
        return num % 9
