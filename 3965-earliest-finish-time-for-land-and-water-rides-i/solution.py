class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        
        # Scenario 1: Land ride first, then Water ride
        for i in range(n):
            land_finish = landStartTime[i] + landDuration[i]
            for j in range(m):
                water_start = max(land_finish, waterStartTime[j])
                water_finish = water_start + waterDuration[j]
                ans = min(ans, water_finish)
                
        # Scenario 2: Water ride first, then Land ride
        for j in range(m):
            water_finish = waterStartTime[j] + waterDuration[j]
            for i in range(n):
                land_start = max(water_finish, landStartTime[i])
                land_finish = land_start + landDuration[i]
                ans = min(ans, land_finish)
                
        return ans
