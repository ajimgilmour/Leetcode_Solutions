# Problem: Find Missing and Repeated Values
# Question ID: 3227
# Difficulty: Easy
# Solved Date: 2025-03-07
# LeetCode URL: https://leetcode.com/problems/find-missing-and-repeated-values/

// https://leetcode.com/problems/find-missing-and-repeated-values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = {}
        m = 0
        l = 0

        for r in grid:
            for n in r:
                d[n] = d.get(n, 0) + 1
                if d[n] >= 2 and m == 0:
                    m = n

        for i in range(1, len(grid) * len(grid) + 1):
            if i not in d.keys():
                l = i
                break

        return [m, l]
