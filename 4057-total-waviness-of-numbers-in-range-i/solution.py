class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            # Waviness is 0 for numbers with fewer than 3 digits
            if len(s) < 3:
                continue
                
            for i in range(1, len(s) - 1):
                # Check for Peak
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    total_waviness += 1
                # Check for Valley
                elif s[i] < s[i-1] and s[i] < s[i+1]:
                    total_waviness += 1
                    
        return total_waviness
