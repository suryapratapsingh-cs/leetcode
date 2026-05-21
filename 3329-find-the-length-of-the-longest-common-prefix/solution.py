class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Step 1: Insert all possible prefixes from arr1 into the hash set
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Strip the last digit to get the next prefix

        max_len = 0

        # Step 2: Check prefixes of elements in arr2 against the hash set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # Update max length found (number of digits)
                    max_len = max(max_len, len(str(num)))
                    break  # Move to next number since shrinking further gives smaller lengths
                num //= 10

        return max_len
