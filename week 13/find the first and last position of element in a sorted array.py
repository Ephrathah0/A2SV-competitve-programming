class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        x = -1
        
        def binarySearch(left, right, first):
            
            nonlocal x
            mid = left + (right-left)//2
            if left > right:
                return -1 if x==-1 else x
            
            if nums[mid] > target:
                return binarySearch(left, mid-1, first)
            elif nums[mid] < target:
                return binarySearch(mid + 1, right, first)
            else:
                if first:
                    right = mid -1
                else:
                    left = mid + 1
                    
                x = mid
                return binarySearch(left, right, first)
        
        left = 0
        right = len(nums)-1
        index = binarySearch(left, right, True)
        
        if index == -1:
            return [-1 ,-1]
        
        return index, binarySearch(left, right, False)
