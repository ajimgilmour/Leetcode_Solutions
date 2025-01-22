# Problem: Happy Number
# Question ID: 202
# Difficulty: Easy
# Solved Date: 2025-01-22
# LeetCode URL: https://leetcode.com/problems/happy-number/

// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        def st(n, visited):
            t = 0
            while(n != 0):
                t += pow(n % 10, 2)
                n //= 10
            if t == 1:
                return True
            if t in visited:
                return False
            visited.add(t)
            return st(t, visited)

        return st(n, set())
        

