# Problem: Counting Words With a Given Prefix
# Question ID: 2292
# Difficulty: Easy
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/counting-words-with-a-given-prefix/

// https://leetcode.com/problems/counting-words-with-a-given-prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
           if i.startswith(pref):
            count += 1
        return count 
