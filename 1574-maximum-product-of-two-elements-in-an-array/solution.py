class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = 0
        for x in nums:
            if x > m1:
                m2 = m1
                m1 = x
            elif x > m2:
                m2 = x
        return (m1 - 1) * (m2 - 1)
