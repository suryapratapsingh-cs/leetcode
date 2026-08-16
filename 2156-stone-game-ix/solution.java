class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] cnt = new int[3];
        for (int stone : stones) {
            cnt[stone % 3]++;
        }

        // If count of stones with remainder 0 is even:
        // Alice wins if there is at least one stone with remainder 1 and at least one with remainder 2.
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }

        // If count of stones with remainder 0 is odd:
        // Alice wins if the absolute difference between count of 1s and 2s is greater than 2.
        return Math.abs(cnt[1] - cnt[2]) > 2;
    }
}
