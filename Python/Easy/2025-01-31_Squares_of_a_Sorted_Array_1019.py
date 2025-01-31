# Problem: Squares of a Sorted Array
# Question ID: 1019
# Difficulty: Easy
# Solved Date: 2025-01-31
# LeetCode URL: https://leetcode.com/problems/squares-of-a-sorted-array/

// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

        return res
