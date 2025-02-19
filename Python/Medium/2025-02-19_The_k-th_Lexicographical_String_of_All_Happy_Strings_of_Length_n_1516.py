# Problem: The k-th Lexicographical String of All Happy Strings of Length n
# Question ID: 1516
# Difficulty: Medium
# Solved Date: 2025-02-19
# LeetCode URL: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        strs = []
        letters = ['a', 'b', 'c']

        def dfs(s):
            if len(s) == n:
                strs.append(s)
                return
            
            for letter in letters:
                if not s or s[-1] != letter:
                    dfs(s + letter)
        
        dfs("")
        strs.sort()
        return strs[k - 1] if k <= len(strs) else ""
