# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count: int = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal count

            if node is None:
                return 
        
            left_result: Optional[int] = dfs(node.left)
            if left_result is not None:
                return left_result
            count += 1
            if count == k:
                return node.val
            
            return dfs(node.right)
        

        return dfs(root)
        