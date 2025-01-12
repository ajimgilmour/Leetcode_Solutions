# Problem: Check if a Parentheses String Can Be Valid
# Question ID: 2221
# Difficulty: Medium
# Solved Date: 2025-01-12
# LeetCode URL: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid

class Solution:
    def canBeValid(self, string: str, lock_status: str) -> bool:
        if len(string) % 2 != 0: 
            return False
        
        open_balance = 0
        for character, lock in zip(string, lock_status):
            if lock == '0' or character == '(':
                open_balance += 1
            elif character == ')':
                open_balance -= 1
            if open_balance < 0:
                return False
        
        close_balance = 0
        for character, lock in zip(reversed(string), reversed(lock_status)):
            if lock == '0' or character == ')':
                close_balance += 1
            elif character == '(':
                close_balance -= 1
            if close_balance < 0:
                return False
        
        return True

