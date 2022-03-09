# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def findTilt(self, root: Optional[TreeNode]) -> int:
        self.totalTilt = 0
        
        def x(node):
            if not node:
                return 0
            left = x(node.left)
            right = x(node.right)
            
            self.totalTilt += abs(left - right)
            return left + right + node.val
        
        x(root)
        return self.totalTilt  
        
