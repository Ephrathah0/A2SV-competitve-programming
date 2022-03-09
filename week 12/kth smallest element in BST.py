# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(root, stack):
            if not root:
                return 0
            
            dfs(root.left,stack)
            stack.append(root.val)
            dfs(root.right,stack)

        dfs(root,stack)
        
        return stack[k-1]
