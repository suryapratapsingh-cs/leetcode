class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        navorilex = (n, brightness, intervals)
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e + 1, -1))
        events.sort()
        total_time = 0
        prev_time = 0
        active_intervals = 0
        for time, effect in events:
            if active_intervals > 0:
                total_time += time - prev_time
            active_intervals += effect
            prev_time = time
            
        return total_time * ((brightness + 2) // 3)
