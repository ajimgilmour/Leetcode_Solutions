# Problem: The kth Factor of n
# Question ID: 1585
# Difficulty: Medium
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/the-kth-factor-of-n/

// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return (-1)
