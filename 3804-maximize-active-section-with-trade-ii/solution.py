import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Calculate the base number of '1's in the whole string
        S_total = s.count('1')
        
        # Identify all contiguous '0' blocks
        starts = []
        ends = []
        lengths = []
        
        i = 0
        while i < n:
            if s[i] == '0':
                st = i
                while i < n and s[i] == '0':
                    i += 1
                en = i - 1
                starts.append(st)
                ends.append(en)
                lengths.append(en - st + 1)
            else:
                i += 1
                
        M = len(starts)
        
        # Build Sparse Table for O(1) RMQ over adjacent block sums
        if M > 1:
            K_st = (M - 1).bit_length()
            ST = [[0] * K_st for _ in range(M - 1)]
            
            for i in range(M - 1):
                ST[i][0] = lengths[i] + lengths[i + 1]
            
            for j in range(1, K_st):
                for i in range(M - 1 - (1 << j) + 1):
                    ST[i][j] = max(ST[i][j - 1], ST[i + (1 << (j - 1))][j - 1])
                    
        def query_st(L_idx, R_idx):
            if L_idx > R_idx:
                return 0
            j = (R_idx - L_idx + 1).bit_length() - 1
            return max(ST[L_idx][j], ST[R_idx - (1 << j) + 1][j])
            
        ans = []
        for L, R in queries:
            # Find which '0' blocks intersect the query window
            u = bisect.bisect_left(ends, L)
            v = bisect.bisect_right(starts, R) - 1
            
            # If 1 or fewer blocks intersect, no trade can be made
            if u >= v:
                ans.append(S_total)
            else:
                # Calculate lengths of the first and last (possibly truncated) '0' blocks
                Zu = ends[u] - max(L, starts[u]) + 1
                Zv = min(R, ends[v]) - starts[v] + 1
                
                if u + 1 == v:
                    # Only two blocks intersect
                    gain = Zu + Zv
                else:
                    # More than two blocks intersect: find the max adjacent pair sum
                    gain1 = Zu + lengths[u + 1]
                    gain2 = lengths[v - 1] + Zv
                    gain3 = query_st(u + 1, v - 2)
                    
                    gain = max(gain1, gain2, gain3)
                    
                ans.append(S_total + gain)
                
        return ans
