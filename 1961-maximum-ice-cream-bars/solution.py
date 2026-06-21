class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        
        for cost in costs:
            freq[cost] += 1
            
        total_bars = 0
        for price in range(1, max_cost + 1):
            if coins < price:
                break
            if freq[price] > 0:
                buy = min(freq[price], coins // price)
                total_bars += buy
                coins -= buy * price
                
        return total_bars
