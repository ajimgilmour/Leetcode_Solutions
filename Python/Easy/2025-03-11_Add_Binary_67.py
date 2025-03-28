# Problem: Add Binary
# Question ID: 67
# Difficulty: Easy
# Solved Date: 2025-03-11
# LeetCode URL: https://leetcode.com/problems/add-binary/

// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return ''.join(s[::-1])
