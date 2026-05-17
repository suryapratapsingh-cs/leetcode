class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            # Mark as visited by flipping the sign
            arr[start] = -arr[start]

            # Explore both jump options
            return self.canReach(arr, start + arr[start]) or self.canReach(
                arr, start - arr[start]
            )

        return False
