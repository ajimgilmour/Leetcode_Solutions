# Problem: Count Prefix and Suffix Pairs I
# Question ID: 3309
# Difficulty: Easy
# Solved Date: 2025-01-08
# LeetCode URL: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                str1 = words[i]
                str2 = words[j]
                if len(str1) > len(str2):
                    continue
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count
