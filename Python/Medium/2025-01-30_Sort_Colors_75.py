# Problem: Sort Colors
# Question ID: 75
# Difficulty: Medium
# Solved Date: 2025-01-30
# LeetCode URL: https://leetcode.com/problems/sort-colors/

// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        idx = 0
        for i in range(3):
            f = d.get(i, 0)
            nums[idx : idx + f] = [i] * f
            idx += f
        
