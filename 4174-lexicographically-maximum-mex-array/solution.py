class Solution:
    def maximumMEX(self, nums: list[int]) -> list[int]:
        from collections import defaultdict
        
        n = len(nums)
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)
        
        result = []
        start = 0
        pos_ptr = defaultdict(int)
        
        while start < n:
            m = 0
            min_end = start - 1
            
            while True:
                lst = positions[m]
                ptr = pos_ptr[m]
                while ptr < len(lst) and lst[ptr] < start:
                    ptr += 1
                pos_ptr[m] = ptr
                
                if ptr >= len(lst):
                    break
                
                min_end = max(min_end, lst[ptr])
                m += 1
            
            if m == 0:
                result.extend([0] * (n - start))
                break
            
            result.append(m)
            start = min_end + 1
        
        return result
