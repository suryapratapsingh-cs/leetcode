class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # 1. Get unique elements and sort them
        sorted_unique = sorted(list(set(arr)))
        
        # 2. Create a dictionary mapping each unique element to its rank
        # Since ranks start at 1, we add 1 to the enumerate index
        rank_map = {val: rank for rank, val in enumerate(sorted_unique, 1)}
        
        # 3. Build the final array by replacing original elements with their rank
        return [rank_map[num] for num in arr]
