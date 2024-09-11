# Problem: Find the Index of the First Occurrence in a String
# Question ID: 28
# Difficulty: Easy
# Solved Date: 2024-09-11
# LeetCode URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
