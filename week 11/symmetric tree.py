# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(a,b):
            if a == None and b == None:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            x =traverse(a.left,b.right)
        
            t= traverse(a.right,b.left)
            
            return a and b
        
        return traverse(root.left,root.right)
    
