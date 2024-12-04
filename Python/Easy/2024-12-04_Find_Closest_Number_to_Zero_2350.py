# Problem: Find Closest Number to Zero
# Question ID: 2350
# Difficulty: Easy
# Solved Date: 2024-12-04
# LeetCode URL: https://leetcode.com/problems/find-closest-number-to-zero/

// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = nums[0]
        for num in nums:
            if abs(num) < abs(closest_num) or (abs(num) == abs(closest_num) and num > closest_num):
                closest_num = num
        return closest_num

