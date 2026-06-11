class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(edges) + 2)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = [(1, -1, 0)]
        max_depth = 0
        
        for node, parent, depth in q:
            max_depth = max(max_depth, depth)
            for neighbor in graph[node]:
                if neighbor != parent:
                    q.append((neighbor, node, depth + 1))
                    
        return pow(2, max_depth - 1, 10**9 + 7)
