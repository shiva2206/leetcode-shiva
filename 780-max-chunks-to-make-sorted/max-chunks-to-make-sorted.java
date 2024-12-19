class Solution {
    HashMap<Integer,Integer> d = new HashMap<>();
    public int maxChunksToSorted(int[] arr) {
        return (int)dfs(0,arr);
    }

    Integer dfs(int i,int[] arr){
        if(i==arr.length) return 0;
        if(d.containsKey(i)) return d.get(i);
        int m = 0;
        int s = 0,req=0;
        for(int j = i;j<arr.length;j++){
            s += arr[j];
            req+= j;
            if(req == s) m = Math.max(m , 1 + dfs(j+1,arr) );
        }
        d.put(i,m);
        return m;
    }
}