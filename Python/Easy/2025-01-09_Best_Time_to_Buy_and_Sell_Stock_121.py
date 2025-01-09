# Problem: Best Time to Buy and Sell Stock
# Question ID: 121
# Difficulty: Easy
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for i in prices:
            mini = min(mini, i)
            maxi = max(maxi, i - mini)
        return maxi
        

