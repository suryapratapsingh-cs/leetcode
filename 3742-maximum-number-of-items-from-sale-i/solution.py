class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        
        # Step 1: Precompute total copies each item contributes (itself + free copies)
        item_data = []
        for i in range(n):
            f_i, p_i = items[i]
            free_count = sum(1 for j in range(n) if i != j and items[j][0] % f_i == 0)
            item_data.append((p_i, 1 + free_count))
        
        # Step 2: Sort items by price descending
        item_data.sort(key=lambda x: x[0], reverse=True)
        
        # Step 3: 0/1 Knapsack DP
        dp = [-1] * (budget + 1)
        dp[0] = 0
        max_copies = 0
        
        for price, value in item_data:
            if price > budget:
                continue
                
            # Check max copies if this item is the minimum-priced item chosen
            for w in range(budget - price + 1):
                if dp[w] != -1:
                    rem_budget = budget - (w + price)
                    extra_copies = rem_budget // price
                    max_copies = max(max_copies, dp[w] + value + extra_copies)
            
            # Update DP array to include the current item for future choices
            for w in range(budget, price - 1, -1):
                if dp[w - price] != -1:
                    dp[w] = max(dp[w], dp[w - price] + value)
                    
        return max_copies
