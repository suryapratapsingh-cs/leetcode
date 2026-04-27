class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: 0: up, 1: right, 2: down, 3: left
        # shapes[type] = {available_directions}
        shapes = {
            1: {1, 3}, 2: {0, 2}, 3: {2, 3},
            4: {1, 2}, 5: {0, 3}, 6: {0, 1}
        }
        # Mapping directions to coordinate changes and their opposite directions
        moves = {0: (-1, 0, 2), 1: (0, 1, 3), 2: (1, 0, 0), 3: (0, -1, 1)}

        queue = collections.deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True
            
            for d in shapes[grid[r][c]]:
                dr, dc, opposite_d = moves[d]
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if the neighbor has a pipe connecting back to the current cell
                    if opposite_d in shapes[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        return False
