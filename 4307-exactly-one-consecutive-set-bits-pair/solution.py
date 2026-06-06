class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        x = n & (n >> 1)
        return x != 0 and (x & (x - 1)) == 0
