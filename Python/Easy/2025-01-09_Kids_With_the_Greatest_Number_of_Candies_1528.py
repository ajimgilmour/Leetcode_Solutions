# Problem: Kids With the Greatest Number of Candies
# Question ID: 1528
# Difficulty: Easy
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = max(candies)
        for i in candies:
            if i + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
