# Problem: Product of the Last K Numbers
# Question ID: 1477
# Difficulty: Medium
# Solved Date: 2025-02-14
# LeetCode URL: https://leetcode.com/problems/product-of-the-last-k-numbers/

// https://leetcode.com/problems/product-of-the-last-k-numbers

import numpy as np

class ProductOfNumbers:

    def __init__(self):
        self.stack = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stack = [1]
        else:
            self.stack.append(self.stack[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.stack):
            return 0
        else:
            return self.stack[-1] // self.stack[-(k+1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
