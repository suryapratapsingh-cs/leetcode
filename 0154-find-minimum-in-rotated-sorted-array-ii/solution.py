class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                # Minimum must be in the right unsorted part
                low = mid + 1
            elif nums[mid] < nums[high]:
                # Minimum is at mid or to the left
                high = mid
            else:
                # When nums[mid] == nums[high], duplicate exists. 
                # Safely reduce the search space by shifting the high pointer.
                high -= 1
                
        return nums[low]
