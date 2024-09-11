# Problem: Sqrt(x)
# Question ID: 69
# Difficulty: Easy
# Solved Date: 2024-09-11
# LeetCode URL: https://leetcode.com/problems/sqrtx/

// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right
        
        
