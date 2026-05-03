class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths differ, s can never become goal
        if len(s) != len(goal):
            return False
        
        # Check if goal exists within the doubled string
        return goal in (s + s)
