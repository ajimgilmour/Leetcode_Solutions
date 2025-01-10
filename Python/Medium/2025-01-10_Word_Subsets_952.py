# Problem: Word Subsets
# Question ID: 952
# Difficulty: Medium
# Solved Date: 2025-01-10
# LeetCode URL: https://leetcode.com/problems/word-subsets/

// https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        map1 = dict()
        res = []

        for word in words2:
            for letter in word:
                map1[letter] = max(map1.get(letter, 0), word.count(letter))

        for words in words1:
            word_count = dict() 
            for letter in words:
                word_count[letter] = word_count.get(letter, 0) + 1
            
            count = 0
            for letter in map1:
                if word_count.get(letter, 0) >= map1[letter]: 
                    count += 1
            
            if count == len(map1):
                res.append(words)

        return res
