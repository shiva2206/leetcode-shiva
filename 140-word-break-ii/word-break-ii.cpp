class Solution {
public:
    vector<string> res,l;
    unordered_set<string> dic;
    void dfs(int i,string s){
        if(i==s.size()){
            int t = true;
            string a = "";
            for(string b : l){
                if(t){
                    a+=b;
                    t = false;
                }else{
                    a+= " "+b;
                }
            }
            res.push_back(a);
            return ;
        }

        string q = "";
        for(int j = i;j<s.length();j++){
            q += s[j];
            if(dic.count(q)==1){
                l.push_back(q);
                dfs(j+1,s);
                l.pop_back();
            }
        }
        return ;
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        for(string a : wordDict){
            dic.insert(a);
        }
        dfs(0,s);
        return res;
    }
};