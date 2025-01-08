# Problem: Is Subsequence
# Question ID: 392
# Difficulty: Easy
# Solved Date: 2025-01-08
# LeetCode URL: https://leetcode.com/problems/is-subsequence/

// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

