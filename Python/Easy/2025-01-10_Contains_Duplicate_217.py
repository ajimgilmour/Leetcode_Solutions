# Problem: Contains Duplicate
# Question ID: 217
# Difficulty: Easy
# Solved Date: 2025-01-10
# LeetCode URL: https://leetcode.com/problems/contains-duplicate/

// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = dict()
        for num in nums:
            if num in num_count:
                return True
            num_count[num] = 1
        return False
