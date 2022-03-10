 def traverse(a,b):
            if a == None and b == None:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            x =traverse(a.left,b.right)
        
            y= traverse(a.right,b.left)
            
            return x and y
        
        return traverse(root.left,root.right)
