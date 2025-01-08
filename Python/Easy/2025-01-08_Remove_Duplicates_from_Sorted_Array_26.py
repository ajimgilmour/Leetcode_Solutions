# Problem: Remove Duplicates from Sorted Array
# Question ID: 26
# Difficulty: Easy
# Solved Date: 2025-01-08
# LeetCode URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        #print(nums)
        return count

