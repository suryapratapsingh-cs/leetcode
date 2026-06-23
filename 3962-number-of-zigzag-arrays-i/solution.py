class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # Base case for length 2
        # ends_up: count of valid sequences ending with an upward step (prev < curr)
        # ends_down: count of valid sequences ending with a downward step (prev > curr)
        ends_up = [i for i in range(m)]
        ends_down = [m - 1 - i for i in range(m)]
        
        # Build sequences from length 3 up to n
        for _ in range(3, n + 1):
            new_ends_up = [0] * m
            new_ends_down = [0] * m
            
            # To go UP, previous step must have gone DOWN ending at some value < current
            pref = 0
            for v in range(m):
                new_ends_up[v] = pref
                pref = (pref + ends_down[v]) % MOD
                
            # To go DOWN, previous step must have gone UP ending at some value > current
            suff = 0
            for v in range(m - 1, -1, -1):
                new_ends_down[v] = suff
                suff = (suff + ends_up[v]) % MOD
                
            ends_up, ends_down = new_ends_up, new_ends_down
            
        return (sum(ends_up) + sum(ends_down)) % MOD
