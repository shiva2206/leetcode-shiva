class Solution {
    public int minOperations(String[] logs) {
        int ans = 0;
        for(String s : logs){
            if(s.startsWith("..")) ans-=1;
            else if(!s.startsWith(".")) ans+=1;
            if(ans<0) ans=0;
        }
        return ans;
    }
}