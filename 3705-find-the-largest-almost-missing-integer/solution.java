class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        int[] freq = new int[51]; // Based on constraint: 0 <= nums[i] <= 50
        
        // Count frequencies of all elements
        for (int num : nums) {
            freq[num]++;
        }
        
        // Case 1: k == n
        // Every element appears in exactly 1 subarray (the whole array)
        if (k == n) {
            int max = -1;
            for (int num : nums) {
                max = Math.max(max, num);
            }
            return max;
        }
        
        // Case 2: k == 1
        // Subarrays are single elements. We need the max element with frequency 1
        if (k == 1) {
            int max = -1;
            for (int num : nums) {
                if (freq[num] == 1) {
                    max = Math.max(max, num);
                }
            }
            return max;
        }
        
        // Case 3: 1 < k < n
        // Only nums[0] and nums[n-1] can possibly appear in exactly 1 subarray
        int max = -1;
        if (freq[nums[0]] == 1) {
            max = Math.max(max, nums[0]);
        }
        if (freq[nums[n - 1]] == 1) {
            max = Math.max(max, nums[n - 1]);
        }
        
        return max;
    }
}

