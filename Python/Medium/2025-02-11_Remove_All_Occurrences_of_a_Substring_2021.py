# Problem: Remove All Occurrences of a Substring
# Question ID: 2021
# Difficulty: Medium
# Solved Date: 2025-02-11
# LeetCode URL: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

// https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        left = 0
        res = list(s)

        while left < len(res):
            temp = (''.join(res[left:left+len(part)]))
            if len(temp) == len(part) and str(temp) == part:
                del res[left:left+len(part)]
                left = max(0, left - len(part))
            else:
                left += 1

        return (''.join(res))


