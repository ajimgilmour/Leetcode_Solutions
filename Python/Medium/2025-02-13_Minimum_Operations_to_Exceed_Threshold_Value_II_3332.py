# Problem: Minimum Operations to Exceed Threshold Value II
# Question ID: 3332
# Difficulty: Medium
# Solved Date: 2025-02-13
# LeetCode URL: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if all(x >= k for x in nums):
            return 0
            
        heapq.heapify(nums)
        count = 0
    
        while len(nums) > 1:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            
            new = first * 2 + second
            heapq.heappush(nums, new)
            
            count += 1

            if all(x >= k for x in nums):
                return count

        return count   
