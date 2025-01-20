# Problem: First Completely Painted Row or Column
# Question ID: 2685
# Difficulty: Medium
# Solved Date: 2025-01-20
# LeetCode URL: https://leetcode.com/problems/first-completely-painted-row-or-column/

// https://leetcode.com/problems/first-completely-painted-row-or-column

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        d = {}

        for i in range(rows):
            for j in range(cols):
                d[mat[i][j]] = (i, j)
        
        rc = [0] * rows
        cc = [0] * cols
        print(rc, cc)

        for i, val in enumerate(arr):
            r, c = d[val]
            rc[r] += 1
            cc[c] += 1
            if rc[r] == cols or cc[c] == rows:
                return i

        return len(arr) - 1
