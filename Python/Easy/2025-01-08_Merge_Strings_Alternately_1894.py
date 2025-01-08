# Problem: Merge Strings Alternately
# Question ID: 1894
# Difficulty: Easy
# Solved Date: 2025-01-08
# LeetCode URL: https://leetcode.com/problems/merge-strings-alternately/

// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        return("".join(res))
        
        
