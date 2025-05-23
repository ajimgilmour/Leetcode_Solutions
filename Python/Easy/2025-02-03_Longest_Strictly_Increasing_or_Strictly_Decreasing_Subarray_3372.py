# Problem: Longest Strictly Increasing or Strictly Decreasing Subarray
# Question ID: 3372
# Difficulty: Easy
# Solved Date: 2025-02-03
# LeetCode URL: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = dec_len = max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i-1]:
                dec_len += 1
                inc_len = 1
            else:
                inc_len = dec_len = 1
            max_len = max(max_len, inc_len, dec_len)
        return max_len
