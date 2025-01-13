# Problem: Ransom Note
# Question ID: 383
# Difficulty: Easy
# Solved Date: 2025-01-13
# LeetCode URL: https://leetcode.com/problems/ransom-note/

// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for m in magazine:
            if m not in d:
                d[m] = 1
            else:
                d[m] += 1
        for r in ransomNote:
            if r not in d or d[r] == 0:
                return False
            d[r] -= 1

        return True
