# Problem: Remove All Adjacent Duplicates In String
# Question ID: 1128
# Difficulty: Easy
# Solved Date: 2025-02-22
# LeetCode URL: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)

