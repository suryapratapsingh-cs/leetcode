class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Step 1: Linearize the points
        linear_points = []
        for x, y in points:
            if y == 0:
                d = x
            elif x == side:
                d = side + y
            elif y == side:
                d = 2 * side + (side - x)
            else: # x == 0
                d = 3 * side + (side - y)
            linear_points.append(d)
        
        linear_points.sort()
        n = len(linear_points)
        perimeter = 4 * side

        def check(dist):
            # Try starting from different points to handle the cyclic nature
            # Checking the first 'n' points is overkill, but because k is small,
            # we only need to ensure we don't miss a starting configuration.
            # Usually checking points within the first 'dist' is enough.
            for i in range(n):
                # Optimization: if the gap between first and last points 
                # in a potential set is too small, we can't close the loop.
                # However, a simple greedy check from each starting point works:
                count = 1
                last_pos = linear_points[i]
                first_pos = linear_points[i]
                
                curr = i
                for _ in range(k - 1):
                    # Find next point at least 'dist' away
                    target = last_pos + dist
                    # Binary search for the next point
                    idx = bisect_left(linear_points, target)
                    
                    # If not found in current array, wrap around
                    if idx == n:
                        # This start index 'i' cannot satisfy k points
                        count = -1 
                        break
                    
                    last_pos = linear_points[idx]
                    count += 1
                
                # Check if the distance between the last and first point (cyclic) is >= dist
                if count == k and (perimeter - (last_pos - first_pos)) >= dist:
                    return True
                
                # If the first point is too far in, we've checked enough starts
                if linear_points[i] - linear_points[0] > dist:
                    break
            return False

        # Step 2: Binary Search on the result
        low, high = 0, 2 * side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid == 0 or check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
