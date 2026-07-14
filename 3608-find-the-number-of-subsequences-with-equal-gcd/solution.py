import math
from collections import defaultdict
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp stores the frequencies of the GCD pairs (gcd1, gcd2).
        # We use 0 to represent an empty subsequence.
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            new_dp = defaultdict(int)
            for (g1, g2), count in dp.items():
                # 1. Skip the current element (neither subsequence takes it)
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + count) % MOD
                
                # 2. Add current element to the first subsequence
                ng1 = math.gcd(g1, x) if g1 != 0 else x
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + count) % MOD
                
                # 3. Add current element to the second subsequence
                ng2 = math.gcd(g2, x) if g2 != 0 else x
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + count) % MOD
                
            dp = new_dp
            
        # Sum up all configurations where both non-empty subsequences have the same GCD
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans
