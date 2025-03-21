# Problem: Duplicate Zeros
# Question ID: 1168
# Difficulty: Easy
# Solved Date: 2025-03-21
# LeetCode URL: https://leetcode.com/problems/duplicate-zeros/

// https://leetcode.com/problems/duplicate-zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        original = arr[:]
        
        i, j = 0, 0
        n = len(arr)

        while i < n:
            arr[i] = original[j]

            if original[j] == 0:
                if i + 1 < n:
                    arr[i + 1] = 0
                    i += 1
                    
            i += 1
            j += 1
