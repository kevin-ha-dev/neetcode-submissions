# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if node is None:
                return True

            # Conditional range for each node
            if not (lower < node.val < upper):
                return False
            
            # Checks one node at a time starting from left tree
            left_valid: bool = dfs(node.left, lower, node.val)
            right_valid: bool = dfs(node.right, node.val, upper)


            # Both subtrees must be valid
            return left_valid and right_valid
    
        return dfs(root, float("-inf"), float("inf"))