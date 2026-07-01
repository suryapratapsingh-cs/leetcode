class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Array to store the last seen indices of 'a', 'b', and 'c'
        last_seen = [-1, -1, -1]
        count = 0
        
        for i, char in enumerate(s):
            # Update the last seen index of the current character
            last_seen[ord(char) - ord('a')] = i
            
            # If all three characters have been seen at least once
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                # The number of valid substrings ending at the current index 'i'
                # is bounded by the smallest last-seen index plus one.
                count += min(last_seen) + 1
                
        return count
