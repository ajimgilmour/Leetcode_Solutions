# Problem: Max Consecutive Ones
# Question ID: 485
# Difficulty: Easy
# Solved Date: 2025-01-31
# LeetCode URL: https://leetcode.com/problems/max-consecutive-ones/

// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > maxi:
                    maxi = count
            else:
                count = 0
                continue
        return maxi
