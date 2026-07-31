class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        
        # Sort in descending order
        freq.sort(reverse=True)
        
        total_pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            # Determine cost multiplier: 1st 8 letters cost 1 push, 2nd 8 cost 2, etc.
            pushes_per_char = (i // 8) + 1
            total_pushes += freq[i] * pushes_per_char
            
        return total_pushes
