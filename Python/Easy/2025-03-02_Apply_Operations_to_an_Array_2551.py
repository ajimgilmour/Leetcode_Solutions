# Problem: Apply Operations to an Array
# Question ID: 2551
# Difficulty: Easy
# Solved Date: 2025-03-02
# LeetCode URL: https://leetcode.com/problems/apply-operations-to-an-array/

// https://leetcode.com/problems/apply-operations-to-an-array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums

