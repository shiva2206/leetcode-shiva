class Solution {
public:
    vector<int> l;
    int dfs(vector<int>& nums,int k,int i){
        if(i==nums.size()) return (l.size()>0)?1:0;
        int m = dfs(nums,k,i+1);
        if(find(l.begin(),l.end(),nums[i]-k) ==l.end()){
            l.push_back(nums[i]);
            m+= dfs(nums,k,i+1);
            l.pop_back();
        }
        return m;
    }
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return dfs(nums,k,0);
    }
};