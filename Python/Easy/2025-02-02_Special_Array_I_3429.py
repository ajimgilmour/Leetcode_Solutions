# Problem: Special Array I
# Question ID: 3429
# Difficulty: Easy
# Solved Date: 2025-02-02
# LeetCode URL: https://leetcode.com/problems/special-array-i/

// https://leetcode.com/problems/special-array-i

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0 and nums[i - 1] % 2 == 0 or nums[i] % 2 != 0 and nums[i - 1] % 2 != 0 :
                return False
        return True
