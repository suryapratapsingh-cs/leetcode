from typing import List


class Solution:

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # For n >= 3, all numbers from 0 to 2^(bit_length) - 1 can be formed.
        return 1 << n.bit_length()
