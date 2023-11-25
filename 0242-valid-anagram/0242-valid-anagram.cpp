class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        unordered_map<char,int> hm;
        for(int i=0;i<s.length();i++){
            if(hm.find(s[i])==hm.end()) hm[s[i]]=0;
            if(hm.find(t[i])==hm.end()) hm[t[i]]=0;
            hm[s[i]]+=1;
            hm[t[i]]-=1;
        }
        for(int i=0;i<hm.size();i++){
            if(hm[i]!=0) return false;
        }
        return true;
        
    }
};