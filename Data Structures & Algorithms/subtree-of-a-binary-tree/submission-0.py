# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # No subRoot automatically true
        if not subRoot:
            return True
        # If search failed
        if not root: 
            return False    

        def sameTree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            
            if node1 is None and node2 is None:
                return True
            
            if node1 is None:
                return False
            
            if node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        
        if sameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


