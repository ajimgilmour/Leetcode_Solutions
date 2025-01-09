# Problem: Product of Array Except Self
# Question ID: 238
# Difficulty: Medium
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/product-of-array-except-self/

// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
    
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

    
        
