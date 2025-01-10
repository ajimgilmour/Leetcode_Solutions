# Problem: Jewels and Stones
# Question ID: 782
# Difficulty: Easy
# Solved Date: 2025-01-10
# LeetCode URL: https://leetcode.com/problems/jewels-and-stones/

// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j_count = dict()
        for i in jewels:
            if i in j_count:
                j_count[i] += 1
            else:
                j_count[i] = 1
        for i in stones:
            if i in j_count.keys():
                count += 1
        return count
