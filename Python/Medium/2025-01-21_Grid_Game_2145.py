# Problem: Grid Game
# Question ID: 2145
# Difficulty: Medium
# Solved Date: 2025-01-21
# LeetCode URL: https://leetcode.com/problems/grid-game/

// https://leetcode.com/problems/grid-game

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0][1:])
        btm = 0
        m = max(top, btm)

        for i in range(1, len(grid[0])):
            top -= grid[0][i]
            btm += grid[1][i - 1]
            m = min(m, max(top, btm))

        return m

