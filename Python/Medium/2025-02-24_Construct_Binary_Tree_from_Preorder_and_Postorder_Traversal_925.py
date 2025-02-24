# Problem: Construct Binary Tree from Preorder and Postorder Traversal
# Question ID: 925
# Difficulty: Medium
# Solved Date: 2025-02-24
# LeetCode URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
                return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        stack = [root]
        j = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            if stack[-1].left is None:
                stack[-1].left = node
            else:
                stack[-1].right = node
            
            stack.append(node)

            while stack and stack[-1].val == postorder[j]:
                stack.pop()
                j += 1

        return root
        
