class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        HashSet<Integer> hs = new HashSet<>();
        for(int i : banned) hs.add(i);
        int tot = 0, s = 0;
        for(int i = 1 ;i<=n;i++){
            if(s+i>maxSum) return tot;
            if(!hs.contains(i)){
                tot+=1;
                s+=i;
            }
        }

        return tot;
    }
}