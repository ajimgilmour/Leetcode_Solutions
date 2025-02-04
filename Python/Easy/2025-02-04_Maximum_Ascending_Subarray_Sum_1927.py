# Problem: Maximum Ascending Subarray Sum
# Question ID: 1927
# Difficulty: Easy
# Solved Date: 2025-02-04
# LeetCode URL: https://leetcode.com/problems/maximum-ascending-subarray-sum/

// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                m += nums[i]
            else:
                m = nums[i]
            count = max(count, m) 
        return count
