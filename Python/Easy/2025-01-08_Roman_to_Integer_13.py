# Problem: Roman to Integer
# Question ID: 13
# Difficulty: Easy
# Solved Date: 2025-01-08
# LeetCode URL: https://leetcode.com/problems/roman-to-integer/

// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:

        d = {'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000}
    
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if d[s[i]] < d[s[i+1]] if i+1 < len(s) else 0:
                res -= d[s[i]]
            else:
                res += d[s[i]]

        return res
