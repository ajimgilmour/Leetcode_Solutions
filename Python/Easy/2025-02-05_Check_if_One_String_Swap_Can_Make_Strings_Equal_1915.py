# Problem: Check if One String Swap Can Make Strings Equal
# Question ID: 1915
# Difficulty: Easy
# Solved Date: 2025-02-05
# LeetCode URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        m = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                m.append((s1[i], s2[i]))
            if len(m) > 2:
                return False
        return len(m) == 2 and m[0] == m[1][::-1]
