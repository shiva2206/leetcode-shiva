class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> d;
        for(int i : arr){
            if(d.find(i*2)!=d.end()) return true;
            if(i%2==0 && d.find(i/2)!=d.end()) return true;
            d.insert(i);
        }
        return false;
    }
};