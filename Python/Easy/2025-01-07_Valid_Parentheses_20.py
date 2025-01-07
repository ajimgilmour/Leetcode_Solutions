# Problem: Valid Parentheses
# Question ID: 20
# Difficulty: Easy
# Solved Date: 2025-01-07
# LeetCode URL: https://leetcode.com/problems/valid-parentheses/

// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack and (
                (stack[-1] == '{' and s[i] == '}') or
                (stack[-1] == '(' and s[i] == ')') or
                (stack[-1] == '[' and s[i] == ']')
            ):
                stack.pop()
            else:
                return False 
        
        return len(stack) == 0 
