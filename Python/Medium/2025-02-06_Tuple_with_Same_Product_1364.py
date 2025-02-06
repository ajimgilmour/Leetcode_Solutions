# Problem: Tuple with Same Product
# Question ID: 1364
# Difficulty: Medium
# Solved Date: 2025-02-06
# LeetCode URL: https://leetcode.com/problems/tuple-with-same-product/

// https://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_count = {}
        v = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                t = nums[i] * nums[j]
                if t in product_count:
                    v += 8 * product_count[t]
                    product_count[t] += 1
                else:
                    product_count[t] = 1 
        return v
