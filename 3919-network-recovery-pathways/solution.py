from collections import deque

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online) # Calculate n from the length of the online array
        
        # Build adjacency list filtered by online status of destination/source nodes
        adj = [[] for _ in range(n)]
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
        
        # Precompute in-degrees for standard topological sort 
        in_degree = [0] * n
        for u in range(n):
            if not online[u]:
                continue
            for v, _ in adj[u]:
                in_degree[v] += 1
                
        # Generate topological sort order
        topo_order = []
        q = deque([i for i in range(n) if online[i] and in_degree[i] == 0])
        
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Helper function to check if a path exists where every edge >= mid and total cost <= k
        def check(mid: int) -> bool:
            # dp[i] stores the minimum total cost to reach node i from node 0
            dp = [float('inf')] * n
            dp[0] = 0
            
            # Relax edges in topological order
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                for v, cost in adj[u]:
                    if cost >= mid: # Only consider edges matching our binary search criteria
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Binary search on the answer
        low = 0
        high = max((cost for _, _, cost in edges), default=0)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid      # mid is possible, try to look for a larger minimum edge-cost
                low = mid + 1
            else:
                high = mid - 1 # mid is impossible, reduce target
                
        return ans
