# Problem: Minimum Length of String After Operations
# Question ID: 3455
# Difficulty: Medium
# Solved Date: 2025-01-13
# LeetCode URL: https://leetcode.com/problems/minimum-length-of-string-after-operations/

// https://leetcode.com/problems/minimum-length-of-string-after-operations

class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0
        freq = [0] * 26
        for i in s:
            freq[ord(i) - ord('a')] += 1
        for i in freq:
            if i % 2 == 0 and i >= 3:
                count += i - 2
            elif i % 2 == 1 and i >= 3:
                count += i - 1

        return len(s) - count

