class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        nums.sort()
      
        i  = len(nums)-k
        return str(nums[i])
