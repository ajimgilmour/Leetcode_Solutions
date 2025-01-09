# Problem: Reverse Words in a String
# Question ID: 151
# Difficulty: Medium
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/reverse-words-in-a-string/

// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)
