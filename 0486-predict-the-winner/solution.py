class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def get_max_diff(left, right):
            # Base case: only one element left to pick
            if left == right:
                return nums[left]
            
            # Return cached result if already computed
            if (left, right) in memo:
                return memo[(left, right)]
            
            # If the current player picks the left element, their score increases by nums[left].
            # The opponent will then play optimally on the remaining array nums[left+1...right].
            # So, the net score difference for the current player is nums[left] - opponent's best difference.
            pick_left = nums[left] - get_max_diff(left + 1, right)
            
            # Alternatively, if the current player picks the right element:
            pick_right = nums[right] - get_max_diff(left, right - 1)
            
            # The current player will choose the option that maximizes their score difference
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]
            
        # Player 1 wins if the max difference they can get from the whole array is >= 0
        return get_max_diff(0, n - 1) >= 0
