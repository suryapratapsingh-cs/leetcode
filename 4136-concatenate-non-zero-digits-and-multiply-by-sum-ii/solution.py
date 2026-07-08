import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        
        # 1. Filter out non-zero digits and track their original indices
        nonzero_digits = []
        nonzero_idx = []
        for i, ch in enumerate(s):
            if ch != '0':
                nonzero_digits.append(int(ch))
                nonzero_idx.append(i)
        
        n = len(nonzero_digits)
        
        # 2. Precompute prefix sums for digit sums
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nonzero_digits[i]
            
        # 3. Precompute prefix values for the concatenated number
        pref_val = [0] * (n + 1)
        for i in range(n):
            pref_val[i + 1] = (pref_val[i] * 10 + nonzero_digits[i]) % MOD
            
        # 4. Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        
        # 5. Process each query
        for l, r in queries:
            # Find the range of non-zero elements within s[l..r]
            L = bisect.bisect_left(nonzero_idx, l)
            R = bisect.bisect_right(nonzero_idx, r) - 1
            
            if L > R:
                ans.append(0)
                continue
            
            # Calculate total sum of digits in the range
            digit_sum = pref_sum[R + 1] - pref_sum[L]
            
            # Calculate the concatenated number x modulo MOD
            length = R - L + 1
            x = (pref_val[R + 1] - pref_val[L] * pow10[length]) % MOD
            
            # Compute final answer for this query
            ans.append((x * digit_sum) % MOD)
            
        return ans
