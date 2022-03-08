# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root, stack):
            if root.left:
                validBST(root.left,stack)
            stack.append(root.val)
            if root.right:
                validBST(root.right, stack)
            return stack
        
        
        stack = validBST(root, [])
        if stack == sorted(stack) and len(set(stack)) == len(stack):
            return True
