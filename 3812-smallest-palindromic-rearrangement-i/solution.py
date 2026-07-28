class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # 1. Letters ki counting karo
        count = Counter(s)
        
        left_half = []
        middle = ""
        
        # 2. Alphabetical order me check karo
        for char in sorted(count.keys()):
            freq = count[char]
            # Aadha hissa left side ke liye
            left_half.append(char * (freq // 2))
            
            # Agar odd count hai toh beech me aayega
            if freq % 2 == 1:
                middle = char
                
        left_str = "".join(left_half)
        
        # 3. Left + Middle + Ulta Left (Right half)
        return left_str + middle + left_str[::-1]
