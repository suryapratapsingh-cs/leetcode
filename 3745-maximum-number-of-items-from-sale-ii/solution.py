import math
from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        
        factor_count = defaultdict(int)
        for factor, price in items:
            factor_count[factor] += 1
        
        max_factor = n
        factor_total = defaultdict(int)
        for f in range(1, max_factor + 1):
            for multiple in range(f, max_factor + 1, f):
                factor_total[f] += factor_count[multiple]
        
        two_x_segments = []
        min_price_1x = float('inf')
        
        for factor, price in items:
            f_i = factor_total[factor] - 1
            if f_i > 0:
                two_x_segments.append((price, f_i))
            min_price_1x = min(min_price_1x, price)
        
        two_x_segments.sort()
        
        total_items = 0
        remaining = budget
        
        for price, max_copies in two_x_segments:
            if remaining <= 0:
                break
            if min_price_1x != float('inf') and 2 * min_price_1x < price:
                break
            can_buy = min(max_copies, remaining // price)
            total_items += can_buy * 2
            remaining -= can_buy * price
        
        if remaining > 0 and min_price_1x != float('inf'):
            total_items += remaining // min_price_1x
        
        return total_items
