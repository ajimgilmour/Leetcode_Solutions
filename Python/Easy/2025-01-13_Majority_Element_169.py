# Problem: Majority Element
# Question ID: 169
# Difficulty: Easy
# Solved Date: 2025-01-13
# LeetCode URL: https://leetcode.com/problems/majority-element/

// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        m = 0
        ind = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] > m:
                m = d[i]
                ind = i

        return ind

