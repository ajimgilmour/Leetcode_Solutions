# Problem: Number of Distinct Averages
# Question ID: 2561
# Difficulty: Easy
# Solved Date: 2025-03-14
# LeetCode URL: https://leetcode.com/problems/number-of-distinct-averages/

// https://leetcode.com/problems/number-of-distinct-averages

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        uniq_avg = set()
        nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            uniq_avg.add(avg)

            left += 1
            right -= 1

        return len(uniq_avg)
