class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # dp[i] stores the maximum length of suffix of word2 that can be 
        # matched starting from index i in word1 onwards.
        dp = [0] * (n + 1)
        
        # Precompute suffix match lengths from right to left
        matched = 0
        for i in range(n - 1, -1, -1):
            if matched < m and word1[i] == word2[m - 1 - matched]:
                matched += 1
            dp[i] = matched
            
        ans = []
        changed = False
        j = 0 # pointer for word2
        
        for i in range(n):
            if j < m and word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and j < m and dp[i + 1] >= m - (j + 1):
                # Use our one allowed change here
                ans.append(i)
                changed = True
                j += 1
                
            if j == m:
                return ans
                
        return []
