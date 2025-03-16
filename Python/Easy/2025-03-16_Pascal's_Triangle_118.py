# Problem: Pascal's Triangle
# Question ID: 118
# Difficulty: Easy
# Solved Date: 2025-03-16
# LeetCode URL: https://leetcode.com/problems/pascals-triangle/

// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res
