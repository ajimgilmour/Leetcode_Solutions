# Problem: Final Prices With a Special Discount in a Shop
# Question ID: 1570
# Difficulty: Easy
# Solved Date: 2025-02-22
# LeetCode URL: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res
