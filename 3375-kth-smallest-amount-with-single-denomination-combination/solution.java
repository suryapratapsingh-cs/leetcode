class Solution {
    public long findKthSmallest(int[] coins, int k) {
        int n = coins.length;
        long minCoin = coins[0];
        for (int c : coins) {
            minCoin = Math.min(minCoin, c);
        }
        
        int maxMask = 1 << n;
        long[] lcms = new long[maxMask];
        int[] setBits = new int[maxMask];
        
        // Precompute the LCM for every possible combination of coins
        for (int mask = 1; mask < maxMask; mask++) {
            long currentLcm = 1;
            int bits = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    bits++;
                    currentLcm = lcm(currentLcm, coins[i]);
                }
            }
            lcms[mask] = currentLcm;
            setBits[mask] = bits;
        }
        
        // Binary search for the kth smallest amount
        long left = 1;
        long right = (long) k * minCoin;
        long ans = right;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            
            if (count(mid, lcms, setBits, maxMask) >= k) {
                ans = mid;
                right = mid - 1; // Try to find a smaller valid value
            } else {
                left = mid + 1;
            }
        }
        
        return ans;
    }
    
    // Uses Principle of Inclusion-Exclusion to count valid multiples <= x
    private long count(long x, long[] lcms, int[] setBits, int maxMask) {
        long res = 0;
        for (int mask = 1; mask < maxMask; mask++) {
            // Odd number of elements -> add, Even number of elements -> subtract
            if (setBits[mask] % 2 == 1) {
                res += x / lcms[mask];
            } else {
                res -= x / lcms[mask];
            }
        }
        return res;
    }
    
    // Helper to find Greatest Common Divisor
    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    // Helper to find Least Common Multiple
    private long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }
}
