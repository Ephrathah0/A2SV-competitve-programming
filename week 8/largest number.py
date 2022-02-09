class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        nums = nums[::-1]
        i  = len(nums)-1
        while k: 
            while nums[i] == nums[i-1]:
                i -=1
            i -= 1
            k-=1
                
            print(i)    
