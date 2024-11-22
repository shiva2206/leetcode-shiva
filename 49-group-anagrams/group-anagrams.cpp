class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>  d;
        for(string s : strs){
            vector<int> arr(26,0);
            for(char c : s){
                arr[c-'a']+=1;
            }
            string t= "";
            for(int i=0;i<26;i++){
                t+= to_string(arr[i]);
                if(i!=25){
                    t+=",";
                }

            }
            cout <<t<<endl;
            if(d.find(t)==d.end()){
                
                d[t].push_back(s);
            }else{
                d[t].push_back(s);
            }
        }  

        vector<vector<string>> res;
        for(auto vec : d){
            res.push_back(vec.second);
        }
        return res;

    }
};