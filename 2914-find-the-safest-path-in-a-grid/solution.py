from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end cell has a thief, the safeness factor is 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate min distance to any thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        # Add all thieves to the queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        # Step 2: Dijkstra-like algorithm using a Max-Heap
        # Python's heapq is a min-heap, so we store negative safeness values
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            safe, r, c = heapq.heappop(pq)
            safe = -safe  # Convert back to positive
            
            # If we reached the destination, return the safeness
            if r == n - 1 and c == n - 1:
                return safe
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The path safeness is the bottleneck (minimum) distance 
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(pq, (-new_safe, nr, nc))
                    
        return 0
