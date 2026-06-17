class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Step 1: Forward pass to track lengths
        lengths = []
        curr_len = 0
        
        for char in s:
            if char.islower():
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass # Length remains unchanged
            lengths.append(curr_len)
            
        # If k is out of final bounds
        if k >= curr_len or k < 0:
            return '.'
            
        # Step 2: Backward pass to find the character
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            # Length before the current operation
            prev_len = lengths[i-1] if i > 0 else 0
            
            if char.islower():
                if k == prev_len: # The letter was appended right at this position
                    return char
            elif char == '#':
                k %= prev_len
            elif char == '%':
                k = lengths[i] - 1 - k
                
        return '.'
        
