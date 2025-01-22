# Problem: Check If String Is a Prefix of Array
# Question ID: 2093
# Difficulty: Easy
# Solved Date: 2025-01-22
# LeetCode URL: https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if prefix == s:
                return True
            elif len(prefix) > len(s):
                return False
        return False

