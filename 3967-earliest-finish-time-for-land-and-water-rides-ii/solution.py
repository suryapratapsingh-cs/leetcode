class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def calc(start1, dur1, start2, dur2):
            # Earliest finish time for the first ride
            min_end1 = min(s + d for s, d in zip(start1, dur1))
            
            # Earliest completion time for the second ride 
            return min(max(min_end1, s2) + d2 for s2, d2 in zip(start2, dur2))

        # Check both orders: Land -> Water and Water -> Land
        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )
