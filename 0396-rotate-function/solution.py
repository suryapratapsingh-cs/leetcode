class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        # Calculate F(0)
        f = sum(i * num for i, num in enumerate(nums))
        
        max_f = f
        
        # Iteratively calculate F(1) to F(n-1) using the transition formula
        for k in range(1, n):
            f = f + s - n * nums[n - k]
            if f > max_f:
                max_f = f
                
        return max_f
