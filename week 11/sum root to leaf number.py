# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def sum_tree(root, leaf_sum):
            
            if not root:
                return 0
            # leaf node
            
            leaf_sum += str(root.val)
            
            if not root.left and not root.right:
                return int(leaf_sum)
                    
            
            return sum_tree(root.left, leaf_sum) + sum_tree(root.right, leaf_sum)
            
        return sum_tree(root, "")
