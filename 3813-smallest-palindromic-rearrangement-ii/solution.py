import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        half_counts = {}
        mid_char = ""
        
        # Determine the half counts and the middle character (if any)
        for char, count in counts.items():
            if count % 2 == 1:
                mid_char = char
            half_counts[char] = count // 2
            
        L = sum(half_counts.values())
        
        # Step 2: Compute initial number of permutations for the first half
        # W = L! / (c1! * c2! * ... * cn!)
        W = math.factorial(L)
        for count in half_counts.values():
            W //= math.factorial(count)
            
        # If the total possible distinct permutations are less than k, return empty string
        if W < k:
            return ""
            
        first_half = []
        chars = sorted(half_counts.keys())
        
        # Step 3: Incrementally build the first half
        for _ in range(L):
            for c in chars:
                if half_counts[c] > 0:
                    # Calculate how many permutations are possible if we pick character 'c'
                    # W_next = W * count(c) / Remaining_Length
                    W_next = W * half_counts[c] // L
                    
                    if k <= W_next:
                        # Character 'c' is the right choice for the current position
                        first_half.append(c)
                        half_counts[c] -= 1
                        W = W_next
                        L -= 1
                        break
                    else:
                        # Skip this character and subtract its permutation count from k
                        k -= W_next
                        
        # Step 4: Construct the final palindrome string
        res = "".join(first_half)
        return res + mid_char + res[::-1]
