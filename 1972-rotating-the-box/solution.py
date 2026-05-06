class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        # 1. Apply gravity to each row
        for r in range(m):
            available = n - 1
            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    # Move stone to the rightmost available spot
                    boxGrid[r][c], boxGrid[r][available] = ".", "#"
                    available -= 1
                elif boxGrid[r][c] == '*':
                    # Obstacle blocks everything; reset available pointer
                    available = c - 1
        
        # 2. Rotate the box 90 degrees clockwise
        res = [["" for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]
                
        return res
