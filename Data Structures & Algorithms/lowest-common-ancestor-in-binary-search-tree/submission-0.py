# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Assume a binary tree G exists
        # p and q are 2 nodes in G
        # We know node.left < node.val < node.right

        current: TreeNode = root

        while current:
            if(p.val < current.val and q.val < current.val):
                current = current.left
            elif(p.val > current.val and q.val > current.val):
                current = current.right
            else:
                return current
        