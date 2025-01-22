# Problem: Move Zeroes
# Question ID: 283
# Difficulty: Easy
# Solved Date: 2025-01-22
# LeetCode URL: https://leetcode.com/problems/move-zeroes/

// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

