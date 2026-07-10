from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Pair each number with its original index and sort them
        arr = sorted([(nums[i], i) for i in range(n)])
        
        # pos[i] stores the sorted index of the original node i
        pos = [0] * n
        for i in range(n):
            pos[arr[i][1]] = i
            
        # 2. Determine connected components 
        # (if two adjacent sorted elements have a diff > maxDiff, a new component starts)
        comp = [0] * n
        c = 0
        for i in range(1, n):
            if arr[i][0] - arr[i-1][0] > maxDiff:
                c += 1
            comp[i] = c
            
        # 3. R[i] will store the furthest right reachable index from i in exactly 1 jump
        R = [0] * n
        right = 0
        for left in range(n):
            while right + 1 < n and arr[right + 1][0] - arr[left][0] <= maxDiff:
                right += 1
            R[left] = right
            
        # 4. Build the Binary Lifting table
        LOG = 18  # Since N <= 10^5, 2^17 = 131072 is enough
        up = [[0] * LOG for _ in range(n)]
        
        # Base case: 2^0 = 1 jump
        for i in range(n):
            up[i][0] = R[i]
            
        # DP transitions for 2^k jumps
        for k in range(1, LOG):
            for i in range(n):
                up[i][k] = up[up[i][k-1]][k-1]
                
        # 5. Process Queries
        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            
            # Always jump from left to right
            if pu > pv:
                pu, pv = pv, pu
                
            # Same node distance is 0
            if pu == pv:
                ans.append(0)
                continue
                
            # If they are in different connected components, no path exists
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue
                
            # Count jumps needed
            curr = pu
            steps = 0
            
            # Find the max jumps we can take while remaining strictly to the left of pv
            for k in range(LOG - 1, -1, -1):
                if up[curr][k] < pv:
                    curr = up[curr][k]
                    steps += (1 << k)
                    
            # After finishing the jumps, exactly 1 more jump is needed to reach or pass pv
            ans.append(steps + 1)
            
        return ans
