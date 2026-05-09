class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            elements = []
            r_min, r_max = layer, m - 1 - layer
            c_min, c_max = layer, n - 1 - layer
            
            # 1. Extract (Top -> Left -> Bottom -> Right)
            # Top row
            for c in range(c_min, c_max): elements.append(grid[r_min][c])
            # Right col
            for r in range(r_min, r_max): elements.append(grid[r][c_max])
            # Bottom row
            for c in range(c_max, c_min, -1): elements.append(grid[r_max][c])
            # Left col
            for r in range(r_max, r_min, -1): elements.append(grid[r][c_min])
            
            # 2. Rotate
            # For counter-clockwise, the element at index 'i' moves to 'i-1'.
            # This is equivalent to a right-shift in the array logic.
            net_k = k % len(elements)
            rotated = elements[net_k:] + elements[:net_k]
            
            # 3. Put back in the same order
            idx = 0
            for c in range(c_min, c_max):
                grid[r_min][c] = rotated[idx]
                idx += 1
            for r in range(r_min, r_max):
                grid[r][c_max] = rotated[idx]
                idx += 1
            for c in range(c_max, c_min, -1):
                grid[r_max][c] = rotated[idx]
                idx += 1
            for r in range(r_max, r_min, -1):
                grid[r][c_min] = rotated[idx]
                idx += 1
                
        return grid
