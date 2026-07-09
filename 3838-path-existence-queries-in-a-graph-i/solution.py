from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Array to store the component ID for each node
        component = [0] * n
        
        # Traverse and assign component IDs
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                component[i] = component[i-1]
            else:
                component[i] = component[i-1] + 1
                
        # Answer each query in O(1) time
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans
