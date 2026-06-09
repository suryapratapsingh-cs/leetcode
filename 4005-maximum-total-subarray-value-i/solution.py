class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # The maximum value of any subarray is achieved by taking 
        # the difference between the global maximum and global minimum.
        # We can just pick this optimal subarray k times.
        return (max(nums) - min(nums)) * k
