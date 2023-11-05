class Solution {
    public String decodeAtIndex(String s, int k) {
        int i=0;
        long  t=0;
        for(int x=0;x<s.length();x++){
            if (Character.isDigit(s.charAt(x))){
                t=t*((int)(s.charAt(x))-48);
            }else{
                t=t+1;
            }
            i=x;
            if(t>k) break;
        }

        for(int j=i;i>=0;j--){
            if(Character.isDigit(s.charAt(j))){
                t=t/((int)(s.charAt(j))-48);
                k%=t;
            }else{
                if(k==0 || k==t ) return s.charAt(j)+"";
                t=t-1;
            }
        }
        return  "a";
        
    }
}