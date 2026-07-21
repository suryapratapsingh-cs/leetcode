class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        # Augment s with '1' at both ends
        t = "1" + s + "1"
        
        # Split t into alternating blocks of ('0' or '1', length)
        groups = []
        for char in t:
            if groups and groups[-1][0] == char:
                groups[-1][1] += 1
            else:
                groups.append([char, 1])
        
        max_delta = 0
        
        # Find every '1' group that is surrounded by '0' groups
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                # Check if it has '0' neighbors on both left and right
                if groups[i - 1][0] == '0' and groups[i + 1][0] == '0':
                    delta = groups[i - 1][1] + groups[i + 1][1]
                    max_delta = max(max_delta, delta)
                    
        return initial_ones + max_delta
