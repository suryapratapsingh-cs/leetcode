class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp_score = [[-1] * n for _ in range(n)]
        dp_paths = [[0] * n for _ in range(n)]
        
        dp_score[0][0] = 0
        dp_paths[0][0] = 1
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X' or dp_score[i][j] == -1:
                    continue
                
                current_score = dp_score[i][j]
                current_paths = dp_paths[i][j]
                
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for ni, nj in directions:
                    if ni < n and nj < n and board[ni][nj] != 'X':
                        cell_val = 0 if board[ni][nj] in ('S', 'E') else int(board[ni][nj])
                        next_score = current_score + cell_val
                        
                        if next_score > dp_score[ni][nj]:
                            dp_score[ni][nj] = next_score
                            dp_paths[ni][nj] = current_paths
                        elif next_score == dp_score[ni][nj]:
                            dp_paths[ni][nj] = (dp_paths[ni][nj] + current_paths) % MOD
                            
        if dp_score[n-1][n-1] == -1:
            return [0, 0]
            
        return [dp_score[n-1][n-1], dp_paths[n-1][n-1]]
