"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return 0
        
        elif root.children == []:
            return 1
    
        for child in root.children:
            result = 1 + self.maxDepth(child)
            depth = max(depth, result)
        
        return depth
