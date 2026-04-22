class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) >> 1
        
        lo, hi = 0, m
        
        while lo <= hi:
            i = (lo + hi) >> 1   # partition index in nums1
            j = half - i          # partition index in nums2
            
            # Values just left/right of each partition
            # Use -inf/+inf as sentinels for out-of-bounds
            left1  = nums1[i - 1] if i > 0 else -10**6 - 1
            right1 = nums1[i]     if i < m else  10**6 + 1
            left2  = nums2[j - 1] if j > 0 else -10**6 - 1
            right2 = nums2[j]     if j < n else  10**6 + 1
            
            if left1 <= right2 and left2 <= right1:
                # Perfect partition found
                if (m + n) & 1:          # odd total
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            
            elif left1 > right2:         # i is too far right
                hi = i - 1
            else:                        # i is too far left
                lo = i + 1
