from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        current_cost = 0
        
        # Monotonic deque storing [value, count] from right to left
        dq = deque()
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            count = 1
            # Merge elements smaller than nums[l] into nums[l]
            while dq and dq[0][0] < nums[l]:
                val, cnt = dq.popleft()
                current_cost += (nums[l] - val) * cnt
                count += cnt
            dq.appendleft([nums[l], count])
            
            # Shrink the window from the right if operations exceed k
            while current_cost > k:
                # The rightmost element in the window corresponds to the back of the deque
                current_cost -= (dq[-1][0] - nums[r])
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            # All subarrays starting at `l` and ending at any index in [l, r] are valid
            ans += (r - l + 1)
            
        return ans
