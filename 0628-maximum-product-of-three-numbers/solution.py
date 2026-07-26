class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array to easily access the smallest and largest elements
        nums.sort()
        
        # Return the maximum of the two possible products
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
