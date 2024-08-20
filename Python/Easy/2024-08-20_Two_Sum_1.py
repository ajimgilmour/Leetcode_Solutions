# Problem: Two Sum
# Question ID: 1
# Difficulty: Easy
# Solved Date: 2024-08-20
# LeetCode URL: https://leetcode.com/problems/two-sum/

// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
