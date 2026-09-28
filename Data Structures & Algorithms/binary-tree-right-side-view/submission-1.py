# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can approach this problem using BFS
        # Each level has i elements
        # The last item in each level is a hit
        # Therefore we return a list of the last element in each level

        queue: deque[TreeNode] = deque([root])
        result: list[int] = []
        
        if root is None:
            return result

        while queue:
            level: int = len(queue)
            for i in range(level):
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level - 1:
                    result.append(node.val)
        return result