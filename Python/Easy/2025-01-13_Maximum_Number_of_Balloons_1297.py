# Problem: Maximum Number of Balloons
# Question ID: 1297
# Difficulty: Easy
# Solved Date: 2025-01-13
# LeetCode URL: https://leetcode.com/problems/maximum-number-of-balloons/

// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        d = {'b' : 1, 'a' : 1, 'l' : 2, 'o' : 2, 'n' : 1}
        s_d = {}
        for l in text:
            if l in d:
                s_d[l] = s_d.get(l, 0) + 1

        min_balloons = float('inf')

        for char in d:
            if char in s_d:
                min_balloons = min(min_balloons, s_d[char] // d[char])
            else:
                min_balloons = 0 
                break
        
        return min_balloons
        


