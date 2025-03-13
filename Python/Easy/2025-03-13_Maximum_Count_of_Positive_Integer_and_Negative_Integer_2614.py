# Problem: Maximum Count of Positive Integer and Negative Integer
# Question ID: 2614
# Difficulty: Easy
# Solved Date: 2025-03-13
# LeetCode URL: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        d = {'0' : [], '1' : []}
        for i in nums:
            if i < 0:
                d['0'].append(i)
            elif i > 0:
                d['1'].append(i)
        return max(len(d['0']), len(d['1']))
