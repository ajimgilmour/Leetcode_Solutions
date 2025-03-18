# Problem: Make The String Great
# Question ID: 1666
# Difficulty: Easy
# Solved Date: 2025-03-18
# LeetCode URL: https://leetcode.com/problems/make-the-string-great/

// https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and (stack[-1] != char and stack[-1].lower() == char.lower()):
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
