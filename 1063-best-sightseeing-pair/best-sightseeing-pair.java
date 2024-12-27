class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int m = values[0];
        int ans = 0;
        for(int i=1;i<values.length;i++){
            ans = Math.max(ans,m+values[i]-i);
            m = Math.max(m,values[i]+i);
        }   
        return ans;
    }
}