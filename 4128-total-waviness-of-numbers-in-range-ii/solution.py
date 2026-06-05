from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_waviness(n: int) -> int:
            if n < 100:
                return 0
            s = str(n)
            
            @cache
            def dfs(idx, prev1, prev2, tight, leading):
                if idx == len(s):
                    return 1, 0  # (count of valid numbers, total waviness)
                
                limit = int(s[idx]) if tight else 9
                total_cnt, total_wave = 0, 0
                
                for d in range(limit + 1):
                    nxt_tight = tight and (d == limit)
                    nxt_leading = leading and (d == 0)
                    
                    if nxt_leading:
                        cnt, wave = dfs(idx + 1, -1, -1, nxt_tight, True)
                        total_cnt += cnt
                        total_wave += wave
                    else:
                        # Check if prev1 forms a peak or a valley
                        is_wave = 0
                        if not leading and prev2 != -1:
                            if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                is_wave = 1
                        
                        cnt, wave = dfs(idx + 1, d, prev1, nxt_tight, False)
                        total_cnt += cnt
                        total_wave += wave + is_wave * cnt
                        
                return total_cnt, total_wave
            
            return dfs(0, -1, -1, True, True)[1]
        
        return count_waviness(num2) - count_waviness(num1 - 1)
