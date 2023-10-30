class Solution {
    public int countVowelPermutation(int n) {
        if (n==0) return 0;
        
        long[][] d= new long[2][5];
        Arrays.fill(d[1],1);
       
        for(int i=n-1;i>0;i--){
            d[0][0]=d[1][1];
        
            d[0][1]=(d[1][0]+d[1][2])%1000000007;
        
            d[0][2]=(d[1][0]+d[1][1]+d[1][3]+d[1][4]) %1000000007;
    
            d[0][3]=(d[1][2]+d[1][4])%1000000007;
    
            d[0][4]=d[1][0];
        
            d[1][1]=d[0][1];
            d[1][2]=d[0][2];
            d[1][3]=d[0][3];
            d[1][4]=d[0][4];
            d[1][0]=d[0][0];   
        }                      
        return (int)(Arrays.stream(d[1]).sum()%1000000007);
    }
}