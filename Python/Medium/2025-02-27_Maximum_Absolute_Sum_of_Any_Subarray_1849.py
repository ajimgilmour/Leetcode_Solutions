# Problem: Maximum Absolute Sum of Any Subarray
# Question ID: 1849
# Difficulty: Medium
# Solved Date: 2025-02-27
# LeetCode URL: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        cur_max = 0
        cur_min = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

        return max(abs(max_sum), abs(min_sum))
