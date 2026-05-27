class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Track indices: -1 means not seen yet, -2 means invalid status
        last_lower = {}
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
                # If we see a lowercase after its uppercase, it becomes permanently invalid
                if char.upper() in first_upper:
                    first_upper[char.upper()] = -2
            else:
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        # Check all lowercase characters that also have an uppercase counterpart
        for char, lower_idx in last_lower.items():
            upper_char = char.upper()
            if upper_char in first_upper:
                upper_idx = first_upper[upper_char]
                # Valid only if uppercase wasn't invalidated (-2) and lower comes before upper
                if upper_idx != -2 and lower_idx < upper_idx:
                    special_count += 1
                    
        return special_count
