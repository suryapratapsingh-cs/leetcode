class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        seen_get = seen.get  # cache method lookup
        for i, x in enumerate(nums):
            comp = target - x
            j = seen_get(comp)
            if j is not None:
                return [j, i]
            seen[x] = i
