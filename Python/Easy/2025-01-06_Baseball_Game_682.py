# Problem: Baseball Game
# Question ID: 682
# Difficulty: Easy
# Solved Date: 2025-01-06
# LeetCode URL: https://leetcode.com/problems/baseball-game/

// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o.lstrip('-').isnumeric():
                stack.append(int(o))
            elif o == 'C':
                if stack:
                    stack.pop()
            elif o == 'D':
                stack.append((stack[-1]) * 2)
                print(stack[-1])
            elif o == '+':
                stack.append((stack[-1]) + (stack[-2]))

        return sum(map(int, stack))


