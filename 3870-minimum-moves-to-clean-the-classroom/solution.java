import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();
        
        int startR = -1, startC = -1;
        List<int[]> litters = new ArrayList<>();
        
        // Locate Start position and index all Litter items
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                char ch = classroom[r].charAt(c);
                if (ch == 'S') {
                    startR = r;
                    startC = c;
                } else if (ch == 'L') {
                    litters.add(new int[]{r, c});
                }
            }
        }
        
        int numLitter = litters.size();
        if (numLitter == 0) return 0;
        int targetMask = (1 << numLitter) - 1;
        
        // Track max remaining energy seen for state (r, c, mask)
        int[][][] maxEnergy = new int[m][n][1 << numLitter];
        for (int[][] mat : maxEnergy) {
            for (int[] row : mat) {
                Arrays.fill(row, -1);
            }
        }
        
        // Queue stores {r, c, mask, currentEnergy}
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startR, startC, 0, energy});
        maxEnergy[startR][startC][0] = energy;
        
        int steps = 0;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                int r = curr[0];
                int c = curr[1];
                int mask = curr[2];
                int e = curr[3];
                
                if (mask == targetMask) {
                    return steps;
                }
                
                // Out of energy to make the next move
                if (e == 0) continue;
                
                for (int[] d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];
                    
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || classroom[nr].charAt(nc) == 'X') {
                        continue;
                    }
                    
                    int nextMask = mask;
                    char cell = classroom[nr].charAt(nc);
                    
                    // Check if cell is a litter item
                    if (cell == 'L') {
                        for (int k = 0; k < numLitter; k++) {
                            if (litters.get(k)[0] == nr && litters.get(k)[1] == nc) {
                                nextMask |= (1 << k);
                                break;
                            }
                        }
                    }
                    
                    // Calculate next energy
                    int nextEnergy = e - 1;
                    if (cell == 'R') {
                        nextEnergy = energy;
                    }
                    
                    // Prune state if we've reached (nr, nc, nextMask) with equal or higher energy
                    if (nextEnergy > maxEnergy[nr][nc][nextMask]) {
                        maxEnergy[nr][nc][nextMask] = nextEnergy;
                        queue.offer(new int[]{nr, nc, nextMask, nextEnergy});
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
}
