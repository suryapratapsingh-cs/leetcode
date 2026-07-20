class Solution:

    def shiftGrid(
        self, grid: List[List[int]], k: int
    ) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  # Handle k values larger than total elements

        # Step 1: Flatten 2D grid into a 1D list
        flat = [val for row in grid for val in row]

        # Step 2: Rotate the 1D list to the right by k positions
        if k != 0:
            flat = flat[-k:] + flat[:-k]

        # Step 3: Reconstruct the 2D grid from the shifted 1D list
        return [flat[i * n : (i + 1) * n] for i in range(m)]
