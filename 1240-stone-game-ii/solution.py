class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums to quickly find total stones from index i to the end
        suffix_sums = [0] * n
        suffix_sums[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        # dp(i, m) returns the maximum stones the current player can get starting at index i with current M
        def dp(i, m):
            # Base case: no more piles left
            if i >= n:
                return 0
            
            # If the current player can take all remaining piles, they should take them all
            if i + 2 * m >= n:
                return suffix_sums[i]
                
            if (i, m) in memo:
                return memo[(i, m)]
                
            res = 0
            # Explore all possible moves: taking X piles where 1 <= X <= 2M
            for x in range(1, 2 * m + 1):
                # The stones the current player gets is the total remaining stones 
                # minus the maximum stones the other player can get from the next state.
                opponent_score = dp(i + x, max(m, x))
                res = max(res, suffix_sums[i] - opponent_score)
                
            memo[(i, m)] = res
            return res
            
        # Alice starts first at index 0 with M = 1
        return dp(0, 1)
