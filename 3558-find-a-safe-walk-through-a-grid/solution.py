import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. Pehle dabbe (0,0) par kadam rakhte hi health check karein
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False # Agar shuru mein hi health khatam ho gayi toh game over
            
        # 2. Ek table banayein jo yaad rakhega ki kis dabbe par maximum kitni health bachi thi
        max_health = [[-1] * n for _ in range(m)]
        max_health[0][0] = start_health
        
        # 3. Ek Priority Queue (Min-Heap) banayein taaki hum humesha sabse zyada health wale raste par pehle chalein
        # Python mein hum minus (-) sign lagate hain taaki sabse badi health sabse pehle nikle
        pq = [(-start_health, 0, 0)]
        
        while pq:
            h, r, c = heapq.heappop(pq)
            h = -h  # Health ko wapas positive banayein
            
            # 4. Agar hum aakhiri dabbe (destination) par pahunch gaye hain
            if r == m - 1 and c == n - 1:
                return h >= 1 # Agar health 1 ya usse zyada hai toh True, nahi toh False
                
            # Agar hum is dabbe par pehle isse behtar health ke sath aa chuke hain, toh ise skip karein
            if h < max_health[r][c]:
                continue
                
            # 5. Charo taraf dhyan se dekhein: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Check karein ki naya dabba map ke andar hi hai na?
                if 0 <= nr < m and 0 <= nc < n:
                    # Agle dabbe par jaane ke baad bachi hui health
                    next_health = h - grid[nr][nc]
                    
                    # Agar agle dabbe par jaane ke baad bhi health positive hai aur purane raste se behtar hai
                    if next_health >= 1 and next_health > max_health[nr][nc]:
                        max_health[nr][nc] = next_health
                        heapq.heappush(pq, (-next_health, nr, nc)) # Agle kadam ke liye queue mein dalein
                        
        # Agar saare raste check karne ke baad bhi manzil tak nahi pahunch paaye
        return False
