class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # Initialize DP table with -1 (unreachable)
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell (0,0)
        # grid[0][0] is always 0, so cost is 0, score is 0
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cost_inc = 1 if val > 0 else 0
                score_inc = val
                
                for c in range(k + 1):
                    if dp[i][j][c] == -1: continue
                    
                    # Move Right
                    if j + 1 < n:
                        nc, ns = c + (1 if grid[i][j+1] > 0 else 0), dp[i][j][c] + grid[i][j+1]
                        if nc <= k:
                            dp[i][j+1][nc] = max(dp[i][j+1][nc], ns)
                            
                    # Move Down
                    if i + 1 < m:
                        nc, ns = c + (1 if grid[i+1][j] > 0 else 0), dp[i][j][c] + grid[i+1][j]
                        if nc <= k:
                            dp[i+1][j][nc] = max(dp[i+1][j][nc], ns)
                            
        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1
