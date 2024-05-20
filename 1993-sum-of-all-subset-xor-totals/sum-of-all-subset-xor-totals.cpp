class Solution {
public:
    int dfs(vector<int>& nums,int i,int t){
        if(i==nums.size()) return t;
        return dfs(nums,i+1,t) + dfs(nums,i+1,t^nums[i]);
    }
    int subsetXORSum(vector<int>& nums) {
        return dfs(nums,0,0);
    }
};