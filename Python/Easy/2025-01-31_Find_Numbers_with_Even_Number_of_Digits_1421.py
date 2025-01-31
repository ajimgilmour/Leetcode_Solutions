# Problem: Find Numbers with Even Number of Digits
# Question ID: 1421
# Difficulty: Easy
# Solved Date: 2025-01-31
# LeetCode URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digits = 0
            while i != 0:
                digits += 1
                i //= 10
            if digits % 2 == 0:
                count += 1
        return count
