class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the sum of the longest sequential prefix starting from index 0
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break
        
        # Convert nums to a set for $O(1)$ lookups
        num_set = set(nums)
        
        # Find the smallest integer >= s that is missing from nums
        x = s
        while x in num_set:
            x += 1
            
        return x
        
