class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # diff array covers target sums from 2 up to 2 * limit
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b: a, b = b, a
            
            # 1. Initially assume 2 moves for all target sums [2, 2 * limit]
            diff[2] += 2
            
            # 2. Subtract 1 move for sums reachable with 1 replacement: [a + 1, b + limit]
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1
            
            # 3. Subtract another 1 move for the exact sum (0 moves needed): [a + b]
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        res = n
        curr_moves = 0
        # Iterate through possible sums to find the minimum moves
        for i in range(2, 2 * limit + 1):
            curr_moves += diff[i]
            if curr_moves < res:
                res = curr_moves
                
        return res
