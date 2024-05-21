class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> s = new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {
        dfs(nums,0);
        return res;
    }

    public void dfs(int[] nums,int i){
        if(i==nums.length){
            res.add(new ArrayList<>(s));
            return;
        }
        s.add(nums[i]);
        dfs(nums,i+1);
        s.remove(s.size()-1);
        dfs(nums,i+1);
    }
}