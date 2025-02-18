# Problem: Construct Smallest Number From DI String
# Question ID: 2456
# Difficulty: Medium
# Solved Date: 2025-02-18
# LeetCode URL: https://leetcode.com/problems/construct-smallest-number-from-di-string/

// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        num_stack = []

        for index in range(len(pattern) + 1):
            num_stack.append(index + 1)

            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))

        return "".join(result)
