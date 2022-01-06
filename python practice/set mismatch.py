       
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    
        r=[]
        nums.sort()
        r=[x for x in range(1, len(nums)+1) if x not in nums]
        c=dict(Counter(nums))
        
        d=[]
        d=[ x for x in c.keys() if c[x]==2 ]
        r.insert(0,d[0])
        
        return r
