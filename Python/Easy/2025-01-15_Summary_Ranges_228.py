# Problem: Summary Ranges
# Question ID: 228
# Difficulty: Easy
# Solved Date: 2025-01-15
# LeetCode URL: https://leetcode.com/problems/summary-ranges/

// https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            i += 1
        
        return res       

