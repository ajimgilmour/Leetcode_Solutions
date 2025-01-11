# Problem: Construct K Palindrome Strings
# Question ID: 1502
# Difficulty: Medium
# Solved Date: 2025-01-11
# LeetCode URL: https://leetcode.com/problems/construct-k-palindrome-strings/

// https://leetcode.com/problems/construct-k-palindrome-strings

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        else:
            d = {}
            count = 0
            for letters in s:
                if letters not in d:
                    d[letters] = 1
                else:
                    d[letters] += 1
            for c in d.values():
                if c % 2 == 1:
                    count += 1
            if count > k:
                return False
            else:
                return True
