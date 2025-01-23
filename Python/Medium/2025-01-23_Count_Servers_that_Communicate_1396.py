# Problem: Count Servers that Communicate
# Question ID: 1396
# Difficulty: Medium
# Solved Date: 2025-01-23
# LeetCode URL: https://leetcode.com/problems/count-servers-that-communicate/

// https://leetcode.com/problems/count-servers-that-communicate

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rows = [0] * row
        cols = [0] * col

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        count += 1
        return count
