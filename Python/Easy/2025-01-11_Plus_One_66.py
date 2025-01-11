# Problem: Plus One
# Question ID: 66
# Difficulty: Easy
# Solved Date: 2025-01-11
# LeetCode URL: https://leetcode.com/problems/plus-one/

// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] ==  9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
                
