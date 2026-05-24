class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n
        
        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            
            max_jumps = 1
            
            # Jump Right
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            # Jump Left
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            memo[i] = max_jumps
            return max_jumps
        
        return max(dfs(i) for i in range(n))
