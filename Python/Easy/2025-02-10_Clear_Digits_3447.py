# Problem: Clear Digits
# Question ID: 3447
# Difficulty: Easy
# Solved Date: 2025-02-10
# LeetCode URL: https://leetcode.com/problems/clear-digits/

// https://leetcode.com/problems/clear-digits

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(i)
                
        return ''.join(stack)
