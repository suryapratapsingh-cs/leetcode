import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0
        
        # Step 1: Construct prefixGcd array
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(num, mx))
            
        # Step 2: Sort prefixGcd in non-decreasing order
        prefixGcd.sort()
        
        # Step 3 & 4: Pair smallest and largest elements using two pointers
        total_sum = 0
        left, right = 0, len(prefixGcd) - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
