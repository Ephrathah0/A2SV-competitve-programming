class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            
            small,big = nums[i],nums[i]
            
            for j in range(i + 1, len(nums)):
                if nums[j] < small:
                    small = nums[j]
                    
                if nums[j] > big:
                    big = nums[j]
                    
                result += big - small
                
        return result
