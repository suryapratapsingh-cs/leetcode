class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        from math import gcd
        g = gcd(a, b)
        return sum(1 for i in range(1, g + 1) if g % i == 0)
