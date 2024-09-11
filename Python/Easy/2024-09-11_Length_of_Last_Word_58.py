# Problem: Length of Last Word
# Question ID: 58
# Difficulty: Easy
# Solved Date: 2024-09-11
# LeetCode URL: https://leetcode.com/problems/length-of-last-word/

// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        mod_str = s.split()
        return len(mod_str[len(mod_str)-1])
