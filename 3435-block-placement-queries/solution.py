from bisect import bisect_left, insort
from typing import List

class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, index: int, value: int, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l: int, r: int, node: int, start: int, end: int) -> int:
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(
            self.query(l, r, 2 * node, start, mid),
            self.query(l, r, 2 * node + 1, mid + 1, end)
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Determine upper boundary tracking size
        max_x = min(50000, 3 * len(queries)) + 1
        st = SegmentTree(max_x)
        
        # Sentinels for boundaries
        obstacles = [0, max_x]
        st.update(max_x, max_x, 1, 0, max_x)
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx]
                
                # Split the existing gap
                insort(obstacles, x)
                st.update(x, x - prev_obs, 1, 0, max_x)
                st.update(next_obs, next_obs - x, 1, 0, max_x)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                idx = bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]
                
                # Max gap is the largest gap before prev_obs OR the tail gap up to x
                max_gap = max(st.query(0, prev_obs, 1, 0, max_x), x - prev_obs)
                results.append(max_gap >= sz)
                
        return results
