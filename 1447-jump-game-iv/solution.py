from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Graph: map value to all its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([0])
        visited = {0}
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                # Reached the destination
                if curr == n - 1:
                    return steps
                
                # Get all potential next steps
                neighbors = [curr - 1, curr + 1]
                if arr[curr] in graph:
                    neighbors.extend(graph[arr[curr]])
                    # Crucial optimization: Clear to prevent redundant O(N) scans
                    del graph[arr[curr]] 
                
                for neighbor in neighbors:
                    if 0 <= neighbor < n and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            steps += 1
            
        return -1
