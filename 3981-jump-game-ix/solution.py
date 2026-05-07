class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        # 1. Compute prefix maximums
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], nums[i])
            
        # 2. Compute suffix minimums
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i+1], nums[i])
            
        # 3. Identify partitions (connected components)
        i = 0
        while i < n:
            j = i
            # Find the end of the current component
            while j < n - 1 and pre_max[j] > suf_min[j+1]:
                j += 1
            
            # The maximum of this component is the max in nums[i...j]
            # Since pre_max[j] tracks the max from 0 to j, and we 
            # know everything before i was smaller, pre_max[j] is the component max.
            comp_max = pre_max[j]
            
            for k in range(i, j + 1):
                ans[k] = comp_max
            i = j + 1
            
        return ans
