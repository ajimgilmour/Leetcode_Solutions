# Problem: Find the Prefix Common Array of Two Arrays
# Question ID: 2766
# Difficulty: Medium
# Solved Date: 2025-01-14
# LeetCode URL: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            k = i
            count = 0
            for x in A[:k + 1]:
                if x in B[:k + 1]:
                    count += 1
            res.append(count) 
        return res
