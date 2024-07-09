class Solution {
    public double averageWaitingTime(int[][] customers) {
        double ans = 0;
        int t = 0;
        for(int[] i : customers){
            if(t<i[0]) t = i[0];
            t = t + i[1];
            ans += t - i[0];
        }   
        return ans/customers.length;
    }

}