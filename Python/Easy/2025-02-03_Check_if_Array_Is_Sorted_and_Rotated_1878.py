# Problem: Check if Array Is Sorted and Rotated
# Question ID: 1878
# Difficulty: Easy
# Solved Date: 2025-02-03
# LeetCode URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        return True
