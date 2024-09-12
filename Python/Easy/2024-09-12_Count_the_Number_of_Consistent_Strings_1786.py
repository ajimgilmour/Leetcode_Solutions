# Problem: Count the Number of Consistent Strings
# Question ID: 1786
# Difficulty: Easy
# Solved Date: 2024-09-12
# LeetCode URL: https://leetcode.com/problems/count-the-number-of-consistent-strings/

// https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count
        
