class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        x = -1
        
        def binarySearch(left, right, is_first):
            
            nonlocal x
            mid = left + (right-left)//2
            if left > right:
                return -1 if x==-1 else x
            
            if nums[mid] > target:
                return binarySearch(left, mid-1, is_first)
            elif nums[mid] < target:
                return binary_search(mid + 1, right, is_first)
            else:
                if is_first:
                    right = mid -1
                else:
                    left = mid + 1
                    
                x = mid
                return binarySearch(left, right, is_first)
        
        left = 0
        right = len(nums)-1
        first_index = binarySearch(left, right, True)
        
        if first_index == -1:
            return [-1 ,-1]
        
        return [first_index, binarySearch(left, right, False)]
