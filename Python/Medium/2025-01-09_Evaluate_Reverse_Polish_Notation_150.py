# Problem: Evaluate Reverse Polish Notation
# Question ID: 150
# Difficulty: Medium
# Solved Date: 2025-01-09
# LeetCode URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isnumeric():
                stack.append(int(i))
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif i == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))

        return stack.pop()
            
            
        
