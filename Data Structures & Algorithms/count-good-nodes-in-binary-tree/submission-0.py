# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if node is None:
                return 0

            max_so_far: int = max(node.val, max_so_far)

            current_good: int = 0
            if node.val >= max_so_far:
                current_good = 1
            
            left_count: int = dfs(node.left, max_so_far)
            right_count: int = dfs(node.right, max_so_far)

            return current_good + left_count + right_count
        
        return dfs(root, root.val)
            