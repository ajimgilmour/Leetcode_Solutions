# Problem: Removing Stars From a String
# Question ID: 2470
# Difficulty: Medium
# Solved Date: 2025-03-25
# LeetCode URL: https://leetcode.com/problems/removing-stars-from-a-string/

// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != '*':
                stack.append(i)
            if stack and i == '*':
                stack.pop()
        return ''.join(stack)
