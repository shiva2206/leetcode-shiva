class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int ans = 0,a = 0;
        int i = 0;

        for(int j = 0;j<s.length();j++){
            a = a + Math.abs(s.charAt(j) - t.charAt(j));
            while(a>maxCost){
                a = a - Math.abs(s.charAt(i) - t.charAt(i));
                i+=1;
            }
            ans = Math.max(ans,j-i+1);
        }       
        return ans;
    }
}