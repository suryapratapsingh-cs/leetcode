class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return 0
        
        # Precompute prefix sums for column-wise score calculation
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        # dp[curr_h][prev_h] represents max score at current column
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n):
            next_dp = [[0] * (n + 1) for _ in range(n + 1)]
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        # Current height is lower; gain score from previous column
                        score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        next_dp[curr_h][prev_h] = prev_suffix_max[prev_h][0] + score
                    else:
                        # Current height is higher; gain score from current column
                        score = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        next_dp[curr_h][prev_h] = max(
                            prev_suffix_max[prev_h][curr_h], 
                            prev_max[prev_h][curr_h] + score
                        )
            
            dp = next_dp
            # Update prefix/suffix max for the next column iteration
            for ch in range(n + 1):
                prev_max[ch][0] = dp[ch][0]
                for ph in range(1, n + 1):
                    penalty = max(0, col_sum[i][ph] - col_sum[i][ch])
                    prev_max[ch][ph] = max(prev_max[ch][ph - 1], dp[ch][ph] - penalty)
                
                prev_suffix_max[ch][n] = dp[ch][n]
                for ph in range(n - 1, -1, -1):
                    prev_suffix_max[ch][ph] = max(prev_suffix_max[ch][ph + 1], dp[ch][ph])

        return max(max(row) for row in dp)
