class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        nums = [val for row in grid for val in row]
        nums.sort()
        
        median = nums[len(nums) // 2]
        ops = 0
        
        for n in nums:
            diff = abs(n - median)
            # If the difference isn't divisible by x, it's impossible
            if diff % x != 0:
                return -1
            ops += diff // x
            
        return ops
