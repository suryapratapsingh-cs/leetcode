class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Since duplicates do not change the set of achievable XOR values,
        # we only need to consider the unique values in nums.
        S = list(set(nums))
        
        # Step 1: Compute all unique XOR values from pairs (a, b)
        pair_xors = {a ^ b for i, a in enumerate(S) for b in S[i:]}
        
        # Step 2: Combine pair XORs with a 3rd element c from S
        triplet_xors = {p ^ c for p in pair_xors for c in S}
        
        return len(triplet_xors)
