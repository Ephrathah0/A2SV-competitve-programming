# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        q = collections.deque()
        
        q.append(root)
        
        while q:
            q_len = len(q)
            
            level_nodes = []
            for i in range(q_len):
                node = q.popleft()
                
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_nodes:
                print(level_nodes, float(sum(level_nodes)/len(level_nodes)))
                res.append(sum(level_nodes)/len(level_nodes))
        return res
        
