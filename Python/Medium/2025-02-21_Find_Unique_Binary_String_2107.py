# Problem: Find Unique Binary String
# Question ID: 2107
# Difficulty: Medium
# Solved Date: 2025-02-21
# LeetCode URL: https://leetcode.com/problems/find-unique-binary-string/

// https://leetcode.com/problems/find-unique-binary-string

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(str(nums[0]))
        binary_values = [0] * 2 ** n
        for i in range(len(binary_values)):
            binary_values[i] = format(i, f'0{n}b')
            if binary_values[i] not in nums:
                return binary_values[i]
        
