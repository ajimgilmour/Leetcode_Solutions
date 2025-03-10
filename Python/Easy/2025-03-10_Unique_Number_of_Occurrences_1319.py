# Problem: Unique Number of Occurrences
# Question ID: 1319
# Difficulty: Easy
# Solved Date: 2025-03-10
# LeetCode URL: https://leetcode.com/problems/unique-number-of-occurrences/

// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1

        values_lis = list(d.values())

        return len(values_lis) == len(set(values_lis))  
