class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            # Must not contain invalid digits
            if any(d in s for d in '347'):
                continue
            # Must contain at least one digit that changes the value
            if any(d in s for d in '2569'):
                count += 1
        return count
