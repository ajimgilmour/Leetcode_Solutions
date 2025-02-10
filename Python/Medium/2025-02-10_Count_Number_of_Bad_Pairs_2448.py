# Problem: Count Number of Bad Pairs
# Question ID: 2448
# Difficulty: Medium
# Solved Date: 2025-02-10
# LeetCode URL: https://leetcode.com/problems/count-number-of-bad-pairs/

// https://leetcode.com/problems/count-number-of-bad-pairs

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs
