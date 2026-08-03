class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp array initialized to negative infinity, with a 0 at the end (base case)
        dp = [float('-inf')] * n + [0]
        
        # Traverse backwards
        for i in range(n - 1, -1, -1):
            take = 0
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    # Maximize the relative difference in score
                    dp[i] = max(dp[i], take - dp[i + k])
                    
        # dp[0] represents Alice's max relative score starting at index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
