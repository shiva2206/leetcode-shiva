class Solution {
public:
    int trap(vector<int>& heig) {
        int l = heig[0];
        int r = heig[heig.size()-1];

        int x=0;
        int y=heig.size()-1;
        int ans=0,p;
        while (x<=y){
            if(l<=r){
                l=max(l,heig[x]);
                ans+=max(0,l-heig[x]);
                x+=1;
            }else{
                r=max(r,heig[y]);
                ans+=max(0,r-heig[y]);
                y-=1;
            }

        }
        return ans;
        
    }
};