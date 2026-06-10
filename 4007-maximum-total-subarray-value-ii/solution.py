import heapq

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute logarithm array for O(1) RMQ lookup
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1
            
        num_layers = lg[n] + 1
        st_min = [[0] * num_layers for _ in range(n)]
        st_max = [[0] * num_layers for _ in range(n)]
        
        # Initialize Sparse Table base layers
        for i in range(n):
            st_min[i][0] = nums[i]
            st_max[i][0] = nums[i]
            
        # Build Sparse Table
        for j in range(1, num_layers):
            for i in range(n - (1 << j) + 1):
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
        
        # O(1) Subarray value query: max - min
        def get_val(l, r):
            j = lg[r - l + 1]
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            return mx - mn

        # Max-heap elements: (-value, l, r)
        heap = []
        for l in range(n):
            val = get_val(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))
            
        total_value = 0
        
        # Extract top k largest distinct subarray values
        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            total_value += (-neg_val)
            
            # Since sequence is non-increasing as r moves left, push the next best (l, r-1)
            if r > l:
                next_r = r - 1
                next_val = get_val(l, next_r)
                heapq.heappush(heap, (-next_val, l, next_r))
                
        return total_value
        
