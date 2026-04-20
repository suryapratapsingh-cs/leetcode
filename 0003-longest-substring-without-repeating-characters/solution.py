class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        ans = l = 0
        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1
            last[c] = r
            if r - l + 1 > ans:
                ans = r - l + 1
        return ans
