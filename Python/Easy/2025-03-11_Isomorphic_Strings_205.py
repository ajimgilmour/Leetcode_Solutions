# Problem: Isomorphic Strings
# Question ID: 205
# Difficulty: Easy
# Solved Date: 2025-03-11
# LeetCode URL: https://leetcode.com/problems/isomorphic-strings/

// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapper = {}
        for i in range(len(s)):
            if s[i] in mapper:
                if mapper[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapper.values():
                    return False
                mapper[s[i]] = t[i]
        return True
