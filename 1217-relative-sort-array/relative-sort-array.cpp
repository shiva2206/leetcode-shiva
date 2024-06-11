class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int,int> d ;
        for(int i : arr1){
            d[i]++;
        }   

        vector<int> l;

        for(int i : arr2){
            for(int j = 0;j<d[i];j++){
                l.push_back(i);
            }
            d.erase(i);
        }

        vector<int> p ;
        for(auto [k,v] : d){
            p.push_back(k);
        }

        sort(p.begin(),p.end());

        for(int i : p){
            for(int j=0;j<d[i];j++) l.push_back(i);
        }
        return l;
    }
};