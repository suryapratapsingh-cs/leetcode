class Solution {
    public int longestSubsequence(int[] nums) {
        int totalXor = 0;
        boolean hasNonZero = false;

        for (int num : nums) {
            totalXor ^= num;
            if (num != 0) {
                hasNonZero = true;
            }
        }

        // Case 1: All elements are 0, no subsequence can have a non-zero XOR.
        if (!hasNonZero) {
            return 0;
        }

        // Case 2: XOR of all elements is already non-zero, take the whole array.
        if (totalXor != 0) {
            return nums.length;
        }

        // Case 3: XOR of all elements is 0, but there are non-zero elements.
        // Removing any non-zero element will leave a non-zero XOR.
        return nums.length - 1;
    }
}
