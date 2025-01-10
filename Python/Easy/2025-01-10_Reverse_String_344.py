# Problem: Reverse String
# Question ID: 344
# Difficulty: Easy
# Solved Date: 2025-01-10
# LeetCode URL: https://leetcode.com/problems/reverse-string/

// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        
