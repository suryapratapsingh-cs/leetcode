class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        LOG = 18
        
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        depth = [-1] * (n + 1)
        depth[1] = 0
        up = [[1] * LOG for _ in range(n + 1)]
        
        # BFS to compute depth and immediate parents
        queue = [1]
        for u in queue:
            for v in adj[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.append(v)
                    
        # Compute binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
            
        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                k = depth[u] + depth[v] - 2 * depth[lca]
                ans.append(pow2[k - 1])
                
        return ans
