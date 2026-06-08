class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        ans = [0] * len(nums)
        
        # Count elements less than pivot and equal to pivot
        less_count = 0
        equal_count = 0
        for num in nums:
            if num < pivot:
                less_count += 1
            elif num == pivot:
                equal_count += 1
        
        # Set starting indices for the three categories
        left = 0
        mid = less_count
        right = less_count + equal_count
        
        # Populate the answer array maintaining relative order
        for num in nums:
            if num < pivot:
                ans[left] = num
                left += 1
            elif num == pivot:
                ans[mid] = num
                mid += 1
            else:
                ans[right] = num
                right += 1
                
        return ans
