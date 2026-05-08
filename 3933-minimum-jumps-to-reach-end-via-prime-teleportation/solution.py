from collections import deque

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        max_val = max(nums)
        # Sieve to find primes
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
        
        # Map primes to indices they can reach
        prime_to_indices = {}
        # Pre-calculate which primes divide which numbers
        # to handle the "nums[j] % p == 0" condition
        for i, val in enumerate(nums):
            # Optimization: We only care about primes that actually appear in nums
            # as a jumping catalyst (nums[i] is prime)
            pass 

        # BFS Setup
        queue = deque([(0, 0)]) # (index, distance)
        visited_idx = {0}
        visited_primes = set()
        
        # Build buckets: prime p -> list of indices j where nums[j] % p == 0
        buckets = {}
        for i, val in enumerate(nums):
            # Factorize val to fill buckets
            temp = val
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    buckets.setdefault(d, []).append(i)
                    while temp % d == 0: temp //= d
                d += 1
            if temp > 1:
                buckets.setdefault(temp, []).append(i)

        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # 1. Adjacent Steps
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_idx:
                    visited_idx.add(next_idx)
                    queue.append((next_idx, dist + 1))
            
            # 2. Prime Teleportation
            p = nums[curr_idx]
            if is_prime[p] and p not in visited_primes:
                visited_primes.add(p)
                if p in buckets:
                    for target_idx in buckets[p]:
                        if target_idx not in visited_idx:
                            visited_idx.add(target_idx)
                            queue.append((target_idx, dist + 1))
                    # Clear bucket to ensure O(V + E)
                    buckets[p] = []
                    
        return -1
