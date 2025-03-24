# Problem: Sum of Subarray Ranges
# Question ID: 2227
# Difficulty: Medium
# Solved Date: 2025-03-24
# LeetCode URL: https://leetcode.com/problems/sum-of-subarray-ranges/

// https://leetcode.com/problems/sum-of-subarray-ranges

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(n):
            min_val, max_val = nums[i], nums[i]

            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])

                total_sum += max_val - min_val
        
        return total_sum

