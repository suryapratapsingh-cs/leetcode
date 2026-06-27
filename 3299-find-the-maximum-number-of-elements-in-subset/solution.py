from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_len = 1
        
        if 1 in counts:
            ones = counts[1]
            max_len = max(max_len, ones if ones % 2 != 0 else ones - 1)
            
        seen = set()
        for x in counts:
            if x == 1 or x in seen or counts[x] < 2:
                continue
            
            curr = x
            curr_len = 0
            
            while counts[curr] >= 2:
                seen.add(curr)
                curr_len += 2
                curr *= curr
                
            if counts[curr] >= 1:
                curr_len += 1
            else:
                curr_len -= 1
                
            max_len = max(max_len, curr_len)
            
        return max_len
