import statistics
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        s=[]
        l=[]
        med=[]
        f=[0]*len(nums)
        med.append(statistics.median(nums))
        for i in nums:
            if i>=med[0]:
                l.append(i)
            else:
                s.append(i)
        
        i=1
        for x in s:
            f[i]=x
            i+=2
        i=0
        for x in l:
            f[i]=x
            i+=2
            
        

        return f
                
                
