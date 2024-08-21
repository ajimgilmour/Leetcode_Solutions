# Problem: Palindrome Number
# Question ID: 9
# Difficulty: Easy
# Solved Date: 2024-08-21
# LeetCode URL: https://leetcode.com/problems/palindrome-number/

// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
