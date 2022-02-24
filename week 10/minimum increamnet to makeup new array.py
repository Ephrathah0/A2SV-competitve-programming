class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        arr = []
        
        for x in nums:
            if not arr:
                arr.append(x)
            elif arr[-1] >= x:
                inc = arr[-1] - x + 1
                arr.append(x + inc)
                moves += inc
            else:
                arr.append(x)
            
        return moves
                
        
