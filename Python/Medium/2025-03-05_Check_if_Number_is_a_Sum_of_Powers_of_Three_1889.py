# Problem: Check if Number is a Sum of Powers of Three
# Question ID: 1889
# Difficulty: Medium
# Solved Date: 2025-03-05
# LeetCode URL: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        powers = []
        i = 0
        while 3**i <= n:
            powers.append(3**i)
            i += 1
        
        s = 0
        for i in range(len(powers) - 1, -1, -1):
            if s + powers[i] <= n:
                s += powers[i]
            if s == n:
                return True
        
        return False
        
