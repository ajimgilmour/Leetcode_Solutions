# Problem: Number of Sub-arrays With Odd Sum
# Question ID: 1631
# Difficulty: Medium
# Solved Date: 2025-02-25
# LeetCode URL: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            
            result %= MOD

        return result
