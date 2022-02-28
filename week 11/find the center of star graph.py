class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
      x = edges[0][0]
      y = edges[0][1]
    
        if x in edges[1]:
            return x
        elif y in edges[1]:
            return y
            
        
