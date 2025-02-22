# Problem: Recover a Tree From Preorder Traversal
# Question ID: 1093
# Difficulty: Hard
# Solved Date: 2025-02-22
# LeetCode URL: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        values = traversal.split('-')
        c_nodes = {}
        count = 0
        c_nodes[0] = TreeNode(int(values[0]))
        for value in values[1:]:
            if value:
                node = TreeNode()
                node.val = int(value)
                root = c_nodes[count]

                if root.left is None:
                    root.left = node
                else:
                    root.right = node
                
                c_nodes[count + 1] = node
                count = 0
            else:
                count += 1
        return c_nodes[0]
