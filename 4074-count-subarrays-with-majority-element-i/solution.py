class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Convert to 1 if it matches target, else -1
        # We need subarrays where sum(transformed) > 0
        ans = 0
        cur_sum = 0
        
        # To count pairs (i, j) where cur_sum[j] - cur_sum[i] > 0
        # since constraints are small (N <= 1000), a simple count works.
        # For O(n), we can track frequencies of running balances.
        # Given N <= 1000, even an O(N) auxiliary space frequency map is extremely efficient.
        from collections import defaultdict
        counts = defaultdict(int)
        counts[0] = 1
        
        # For a true O(n) math-based approach, we track how many previous 
        # prefixes have a sum less than the current sum. 
        # Since the sum changes by +/-1, we can maintain the count of valid smaller prefixes.
        smaller_sums_count = 0
        
        for num in nums:
            val = 1 if num == target else -1
            
            if val == 1:
                # cur_sum increases: all previous prefixes with the old cur_sum 
                # are now strictly smaller than the new cur_sum.
                smaller_sums_count += counts[cur_sum]
                cur_sum += 1
            else:
                # cur_sum decreases: prefixes that were equal to the new cur_sum 
                # are no longer smaller than it.
                cur_sum -= 1
                smaller_sums_count -= counts[cur_sum]
                
            ans += smaller_sums_count
            counts[cur_sum] += 1
            
        return ans
