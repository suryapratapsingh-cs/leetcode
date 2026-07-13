class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence = "123456789"
        result = []
        
        # The minimum length of a sequential number is 2 (since low >= 10)
        # The maximum length is 9 (since high <= 10^9)
        for length in range(2, 10):
            for start in range(10 - length):
                # Extract the substring of the current length
                num = int(sequence[start:start + length])
                
                # Check if the generated number is within the range
                if low <= num <= high:
                    result.append(num)
                    
        return result
