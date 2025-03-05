# Problem: Power of Three
# Question ID: 326
# Difficulty: Easy
# Solved Date: 2025-03-05
# LeetCode URL: https://leetcode.com/problems/power-of-three/

// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif  n == 0  or n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3) 
        
        
