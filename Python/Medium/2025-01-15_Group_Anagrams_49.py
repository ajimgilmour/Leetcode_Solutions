# Problem: Group Anagrams
# Question ID: 49
# Difficulty: Medium
# Solved Date: 2025-01-15
# LeetCode URL: https://leetcode.com/problems/group-anagrams/

// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for words in strs[:]:
            w = tuple(sorted(words))
            if w not in d:
                d[w] = []
            d[w].append(words)
            
        return list(d.values())
