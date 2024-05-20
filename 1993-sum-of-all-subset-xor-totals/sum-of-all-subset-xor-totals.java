class Solution {
    public int subsetXORSum(int[] nums) {
         return dfs(nums,0,0);  
    }

    public int dfs(int[] nums,int i,int t){
        if(i==nums.length) return t;
        return dfs(nums,i+1,t) + dfs(nums,i+1,t^nums[i]);
    }
}