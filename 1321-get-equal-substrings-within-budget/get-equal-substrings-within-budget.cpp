class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int ans = 0;
        int a = 0;
        int i = 0;
        for(int j = 0 ;j<s.size();j++){
            a = a + abs(s[j] - t[j]);
            while(a>maxCost){
                a = a - abs(s[i] - t[i]);
                i+=1;
            }
            ans = max(ans,j-i+1);
        }   
        return ans;
    }
};