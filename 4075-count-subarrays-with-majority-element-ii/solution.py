class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def add(self, i: int, delta: int):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Size needed to cover all possible prefix sums from -n to n
        bit = BIT(2 * n + 3)
        offset = n + 2 
        
        ans = 0
        curr_pref = 0
        
        # Add the initial prefix sum of 0
        bit.add(curr_pref + offset, 1)
        
        for num in nums:
            # +1 if it matches the target, -1 otherwise
            curr_pref += 1 if num == target else -1
            
            # Count how many previous prefix sums are strictly less than curr_pref
            ans += bit.query(curr_pref + offset - 1)
            
            # Add current prefix sum to the Fenwick Tree
            bit.add(curr_pref + offset, 1)
            
        return ans
