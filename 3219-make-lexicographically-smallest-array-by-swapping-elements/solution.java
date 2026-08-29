import java.util.*;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        
        // Pair elements with their original indices
        int[][] sortedNums = new int[n][2];
        for (int i = 0; i < n; i++) {
            sortedNums[i][0] = nums[i];
            sortedNums[i][1] = i;
        }
        
        // Sort by element values
        Arrays.sort(sortedNums, (a, b) -> Integer.compare(a[0], b[0]));
        
        int[] result = new int[n];
        int i = 0;
        
        // Process each connected component
        while (i < n) {
            int j = i;
            // Expand component as long as difference between consecutive elements <= limit
            while (j + 1 < n && sortedNums[j + 1][0] - sortedNums[j][0] <= limit) {
                j++;
            }
            
            // Extract indices of the current group and sort them
            int[] indices = new int[j - i + 1];
            for (int k = i; k <= j; k++) {
                indices[k - i] = sortedNums[k][1];
            }
            Arrays.sort(indices);
            
            // Place sorted values into the sorted original positions
            for (int k = i; k <= j; k++) {
                result[indices[k - i]] = sortedNums[k][0];
            }
            
            i = j + 1;
        }
        
        return result;
    }
}
