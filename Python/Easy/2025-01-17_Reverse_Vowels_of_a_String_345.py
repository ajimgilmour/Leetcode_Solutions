# Problem: Reverse Vowels of a String
# Question ID: 345
# Difficulty: Easy
# Solved Date: 2025-01-17
# LeetCode URL: https://leetcode.com/problems/reverse-vowels-of-a-string/

// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        c = "aeiouAEIOU"
        sc = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if sc[left] in c and sc[right] in c:
                sc[left], sc[right] = sc[right], sc[left]
                left += 1
                right -= 1
            elif sc[left] in c:
                right -= 1
            elif sc[right] in c:
                left += 1
            else:
                right -= 1
                left += 1
        
        return ''.join(sc)
            
            
