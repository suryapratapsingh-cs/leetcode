import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Count frequencies of each number in nums
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
        # g[i] will store the EXACT number of pairs whose GCD is i
        g = [0] * (max_val + 1)
        
        # Process from largest possible GCD down to 1
        for i in range(max_val, 0, -1):
            # Count how many numbers in `nums` are multiples of i
            c = 0
            for j in range(i, max_val + 1, i):
                c += cnt[j]
            
            # Total pairs where both elements are multiples of i
            pairs_count = c * (c - 1) // 2
            
            # Subtract pairs whose GCD is a strictly greater multiple of i
            for j in range(2 * i, max_val + 1, i):
                pairs_count -= g[j]
                
            g[i] = pairs_count
            
        # Create a prefix sum array where prefix[i] is the number of pairs with GCD <= i
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + g[i]
            
        # Answer each query using binary search
        ans = []
        for q in queries:
            # bisect_right finds the first index where prefix[idx] > q
            idx = bisect.bisect_right(prefix, q)
            ans.append(idx)
            
        return ans
