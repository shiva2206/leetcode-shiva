class Solution {
public:
    vector<vector<string>> res;
    vector<string> l;
    
    bool isSame(string q){
        int i=0,j=q.size()-1;
        while(i<j){
            if(q[i]!=q[j]) return false;
            i+=1;
            j-=1; 
        }
        return true;
    }
    void dfs(string s,int i){
        if(i==s.size()){
            res.push_back(vector<string>(l));
            return ;
        }

        string q ="";
        for(int k=i;k<s.size();k++){
            q = q+s[k];
            if(isSame(q)){
                l.push_back(q);
                dfs(s,k+1);
                l.pop_back();
            }
        }
        return;
    }
    vector<vector<string>> partition(string s) {
        dfs(s,0);
        return res;
    }
};