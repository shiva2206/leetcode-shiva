class Solution {
public:
    vector<vector<int>> res;
    vector<int> s;

    void dfs(vector<int>& nums,int i){
        if(i==nums.size()){
            res.push_back(vector<int>(s));
            return;
        }
        s.push_back(nums[i]);
        dfs(nums,i+1);
        s.pop_back();
        dfs(nums,i+1);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums,0);
        return res;
    }
};