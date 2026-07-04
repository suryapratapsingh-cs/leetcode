from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        # graph[u] will store tuples of (neighbor, distance)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: BFS to traverse the component containing city 1
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            for neighbor, distance in graph[node]:
                # Track the minimum road distance seen in this component
                min_score = min(min_score, distance)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
