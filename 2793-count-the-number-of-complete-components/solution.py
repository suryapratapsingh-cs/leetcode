from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        complete_count = 0
        
        # Step 2: Find connected components
        for i in range(n):
            if i not in visited:
                component_nodes = []
                queue = deque([i])
                visited.add(i)
                
                # BFS to explore the entire component
                while queue:
                    node = queue.popleft()
                    component_nodes.append(node)
                    
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                # Step 3: Check if the component is complete
                k = len(component_nodes)
                # A component is complete if every node connects to all other (k-1) nodes
                is_complete = all(len(adj[node]) == k - 1 for node in component_nodes)
                
                if is_complete:
                    complete_count += 1
                    
        return complete_count
