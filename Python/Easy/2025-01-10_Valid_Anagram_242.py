# Problem: Valid Anagram
# Question ID: 242
# Difficulty: Easy
# Solved Date: 2025-01-10
# LeetCode URL: https://leetcode.com/problems/valid-anagram/

// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        else:
            for i in set(s):
                if s.count(i) != t.count(i): 
                    return False
            return True

                

