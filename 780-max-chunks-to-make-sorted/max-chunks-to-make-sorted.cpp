class Solution {
public:
    unordered_map<int,int> d; 
    int dfs(int i , vector<int>& arr){
        if(i==arr.size()) return 0;
        if(d.find(i)!=d.end()) return d[i];
        d[i] =0;
        int req = 0,s=0;
        for(int j = i;j<arr.size();j++){
            req+=j;
            s+=arr[j];
            if(req == s) d[i] = max(d[i],1 + dfs(j+1,arr));
        }
        return d[i];
    }
    int maxChunksToSorted(vector<int>& arr) {
        return dfs(0,arr);
    }
};