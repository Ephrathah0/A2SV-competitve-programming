class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * i for i in range(1, len(triangle)+1)]
        
        for i in range(len(triangle)):
            if i == 0: dp[0] = triangle[0]; continue
            for j in range(len(triangle[i])):
                left = dp[i-1][j-1] if j > 0 else math.inf
                right = dp[i-1][j] if j < len(triangle[i-1]) else math.inf
                dp[i][j] = triangle[i][j] + min(left, right)
                
        return min(dp[-1])
