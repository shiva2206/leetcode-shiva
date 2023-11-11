class Solution {
    public int countHomogenous(String s) {
        long tot =1;
        int i=0;
        char t = s.charAt(0);
        for(int j=1;j<s.length();j++){
            if(s.charAt(j)!=t){
                t=s.charAt(j);
                i=j;

            }
            tot+=j-i+1;
        }
        return (int)(tot%1000000007);
    }
}