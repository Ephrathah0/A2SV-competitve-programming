class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numss = set(nums)
        nums.clear()
        nums += list(numss)
        nums.sort()

        return len(numss)
