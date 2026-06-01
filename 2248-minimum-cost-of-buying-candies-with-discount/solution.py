class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort in descending order to maximize the value of free candies
        cost.sort(reverse=True)
        
        # Sum all candies except every 3rd one (index 2, 5, 8, ...)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)
