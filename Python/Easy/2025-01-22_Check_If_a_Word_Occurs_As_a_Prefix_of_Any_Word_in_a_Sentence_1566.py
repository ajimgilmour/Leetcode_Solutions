# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Question ID: 1566
# Difficulty: Easy
# Solved Date: 2025-01-22
# LeetCode URL: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        i = 0
        while i < len(sentence):
            if sentence[i].startswith(searchWord):
                return (i + 1)
            i += 1
        return (-1)
        
        
