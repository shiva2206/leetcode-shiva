class Solution {
    HashMap<Integer,List<Integer>> d = new HashMap<>();
    HashMap<Integer,HashSet<Integer>> dp = new HashMap<>();
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        for(int[] i : edges){
            if(!d.containsKey(i[0])) d.put(i[0],new ArrayList<>());
            if(!d.containsKey(i[1])) d.put(i[1],new ArrayList<>());
            d.get(i[1]).add(i[0]);
        }
        for(int i = 0;i<n;i++){
            ArrayList<Integer> l = new ArrayList(dfs(i));
            Collections.sort(l);
            res.add(l);
        }
        return res;
    }

    public HashSet<Integer> dfs(int i){
        if(dp.containsKey(i)) return dp.get(i);
        dp.put(i,new HashSet<>());
        if(!d.containsKey(i)) return new HashSet<>();
        for(int k : d.get(i)){
            dp.get(i).add(k);
            dp.get(i).addAll(dfs(k));
        }
        return dp.get(i);
    }
}