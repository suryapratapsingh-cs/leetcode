class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        # dp[i] will be True if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # Track the number of reachable indices in the current window
        reachable_count = 0
        
        for i in range(1, n):
            # Add the newly available index to our window
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
                
            # Remove the index that just fell out of our window
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1
                
            # If the current character is '0' and there is at least 
            # one reachable index in our window, then i is reachable
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]
