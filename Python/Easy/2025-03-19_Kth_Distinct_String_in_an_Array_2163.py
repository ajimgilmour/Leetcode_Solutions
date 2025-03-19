# Problem: Kth Distinct String in an Array
# Question ID: 2163
# Difficulty: Easy
# Solved Date: 2025-03-19
# LeetCode URL: https://leetcode.com/problems/kth-distinct-string-in-an-array/

// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1

        distinct = [i for i in arr if d[i] == 1]

        return distinct[k - 1] if k <= len(distinct) else ""
