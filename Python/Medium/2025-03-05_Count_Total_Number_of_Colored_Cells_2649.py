# Problem: Count Total Number of Colored Cells
# Question ID: 2649
# Difficulty: Medium
# Solved Date: 2025-03-05
# LeetCode URL: https://leetcode.com/problems/count-total-number-of-colored-cells/

// https://leetcode.com/problems/count-total-number-of-colored-cells

class Solution:
    def coloredCells(self, n: int) -> int:
        s = 1
        for i in range(1, n):
            s += 4 * i

        return s
