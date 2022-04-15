class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            diff = price - lowest
            temp = max(temp, diff)
        return 
