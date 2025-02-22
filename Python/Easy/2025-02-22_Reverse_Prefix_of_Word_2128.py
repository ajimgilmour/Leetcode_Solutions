# Problem: Reverse Prefix of Word
# Question ID: 2128
# Difficulty: Easy
# Solved Date: 2025-02-22
# LeetCode URL: https://leetcode.com/problems/reverse-prefix-of-word/

// https://leetcode.com/problems/reverse-prefix-of-word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ''
        stack = []

        if ch not in word:
            return word
        idx = 0
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                idx = i
                break
        
        res = ''.join(stack[::-1]) + word[idx + 1:]
        return res
