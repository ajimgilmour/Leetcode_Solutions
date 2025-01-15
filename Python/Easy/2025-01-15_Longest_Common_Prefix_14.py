# Problem: Longest Common Prefix
# Question ID: 14
# Difficulty: Easy
# Solved Date: 2025-01-15
# LeetCode URL: https://leetcode.com/problems/longest-common-prefix/

// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = strs[0]
        i = 0
        l = len(c)

        while(i < len(strs)):
            if c == strs[i][:l]:
                i += 1
            else:
                l -= 1
                c = c[:l]
        return c

            
