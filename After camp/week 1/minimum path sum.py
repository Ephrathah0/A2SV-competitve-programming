class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        
        for x in range(m):
            dp[0][x] = dp[0][x-1] + grid[0][x]
            
        for i in range(1,n):
            for j in range(m):
                up = dp[i-1][j] if i > 0 else math.inf
                left = dp[i][j-1] if j > 0 else math.inf
                dp[i][j] = grid[i][j] + min(up, left)
                
        return dp[-1][-1]
