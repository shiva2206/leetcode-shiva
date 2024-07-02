class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int,int> d;
        for(int i : nums1){
            d[i]++;
        }   
        for(int i : nums2){
            if(d[i]>0){
                d[i]--;
                res.push_back(i);
            }
        }
        return res;
    }
};