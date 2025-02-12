# Problem: Max Sum of a Pair With Equal Sum of Digits
# Question ID: 2473
# Difficulty: Medium
# Solved Date: 2025-02-12
# LeetCode URL: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}

        for i in range(len(nums)):
            s = 0
            t = nums[i]
            while t != 0:
                s += t % 10
                t //= 10
            if s not in d:
                d[s] = []
            d[s].append(nums[i])

        res = -1

        for key in d:
            if len(d[key]) >= 2:
                d[key].sort(reverse=True)
                res = max(res, d[key][0] + d[key][1])

        return res


