# Problem: First Unique Character in a String
# Question ID: 387
# Difficulty: Easy
# Solved Date: 2025-03-22
# LeetCode URL: https://leetcode.com/problems/first-unique-character-in-a-string/

// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i, j in d.items():
            if j == 1:
                return s.index(i)
        return -1
