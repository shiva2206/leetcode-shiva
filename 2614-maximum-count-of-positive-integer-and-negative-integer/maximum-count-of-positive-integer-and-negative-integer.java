class Solution {
    public int maximumCount(int[] nums) {
        
        int n = 0, p=0;
        for(int i : nums){
            if(i>0) p+=1;
            else if(i<0) n+=1;

        }

        return Math.max(p,n);
    }
}