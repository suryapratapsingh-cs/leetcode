class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_val = max(nums)
        # present[i] will store the smallest number from nums that divides i
        # Initialize with infinity
        best_divisor = [float('inf')] * (max_val + 1)
        
        # Mark all numbers actually present in the array as their own best divisor
        unique_nums = set(nums)
        for x in unique_nums:
            best_divisor[x] = x
            
        # Sieve: For each number present in the array, 
        # mark all its multiples with that number as a potential minimum divisor.
        # We iterate from smallest to largest to ensure the smallest divisor sticks.
        for d in sorted(unique_nums):
            # If we've already found a smaller divisor for all multiples of 'd', 
            # we could technically skip, but for simplicity:
            for multiple in range(d * 2, max_val + 1, d):
                if d < best_divisor[multiple]:
                    best_divisor[multiple] = d
                    
        return sum(best_divisor[x] for x in nums)
