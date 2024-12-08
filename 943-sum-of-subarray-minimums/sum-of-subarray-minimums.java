class Solution {
    public int sumSubarrayMins(int[] l) {
        long res =0;
        int mod = 1000000007;
        Stack<Integer> s = new Stack<>();
        int[] arr = new int[l.length+1];
        for(int i =0;i<l.length;i++) arr[i] = l[i];
        arr[l.length] = Integer.MIN_VALUE;
        // arr.add(Integer.MIN_VALUE);
        for(int i =0;i<arr.length;i++){
            while(s.size()>0 && arr[s.peek()]>arr[i]){
                int q = s.pop();
                int lft = q - ((s.size()>0)? s.peek() : -1);
                int rgt = i - q;
                res += ((long)arr[q]*lft*rgt)%mod;
                res %= mod;
            }
            s.add(i);
        }
        res %=mod;
        return (int)res;
    }
}