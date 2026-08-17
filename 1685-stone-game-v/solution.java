class Solution {
    int[][] memo;
    int[] prefixSum;

    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        memo = new int[n][n];
        prefixSum = new int[n + 1];
        
        // Compute prefix sums for O(1) range sum queries
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }
        
        return dfs(0, n - 1);
    }
    
    private int dfs(int left, int right) {
        // Base case: Only one stone left, score is 0
        if (left == right) {
            return 0;
        }
        
        // Return cached result if already computed
        if (memo[left][right] != 0) {
            return memo[left][right];
        }
        
        int maxScore = 0;
        
        // Try all possible ways to divide the current row into two parts
        for (int i = left; i < right; i++) {
            int leftSum = prefixSum[i + 1] - prefixSum[left];
            int rightSum = prefixSum[right + 1] - prefixSum[i + 1];
            
            if (leftSum < rightSum) {
                // Bob throws away the right row, Alice's score increases by leftSum
                maxScore = Math.max(maxScore, leftSum + dfs(left, i));
            } else if (leftSum > rightSum) {
                // Bob throws away the left row, Alice's score increases by rightSum
                maxScore = Math.max(maxScore, rightSum + dfs(i + 1, right));
            } else {
                // Sums are equal, Alice decides which row to throw away
                maxScore = Math.max(maxScore, leftSum + Math.max(dfs(left, i), dfs(i + 1, right)));
            }
        }
        
        // Cache and return the maximum score found
        memo[left][right] = maxScore;
        return maxScore;
    }
}
