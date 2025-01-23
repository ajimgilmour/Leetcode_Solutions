# Problem: Reverse Words in a String III
# Question ID: 557
# Difficulty: Easy
# Solved Date: 2025-01-23
# LeetCode URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/

// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        lis = list(s.split())
        res = []
        for i in range(len(lis)):
           res.append(lis[i][::-1])

        return ' '.join(res)
