# Problem: Spiral Matrix
# Question ID: 54
# Difficulty: Medium
# Solved Date: 2025-01-11
# LeetCode URL: https://leetcode.com/problems/spiral-matrix/

// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return False
        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, columns - 1
        res = []

        while len(res) < rows * columns:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
