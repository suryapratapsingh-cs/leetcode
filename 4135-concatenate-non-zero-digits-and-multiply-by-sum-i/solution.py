class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        x = 0
        digit_sum = 0
        multiplier = 1
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                # Add to the sum of digits
                digit_sum += digit
                # Prepend the digit to x
                x += digit * multiplier
                # Move multiplier to the next decimal place
                multiplier *= 10
            n //= 10
            
        return x * digit_sum
