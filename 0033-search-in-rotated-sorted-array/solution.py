class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Target is in the left sorted half
                else:
                    low = mid + 1   # Target is in the right half
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Target is in the right sorted half
                else:
                    high = mid - 1  # Target is in the left half
                    
        return -1
