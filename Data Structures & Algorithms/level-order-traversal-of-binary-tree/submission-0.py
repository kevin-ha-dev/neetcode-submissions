# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque[TreeNode] = deque([root])

        result: list[list[int]] = []

        if root is None:
            return []

        while queue:
            level: list[int] = []
            level_size: int = len(queue)

            for i in range(level_size):
                node: TreeNode = queue.popleft()
                
                # append current levels children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # append most recent node to level
                level.append(node.val)

            result.append(level)
        
        return result





