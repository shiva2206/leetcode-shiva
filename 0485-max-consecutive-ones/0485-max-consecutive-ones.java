class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int m=0;
        int c=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0) {
                m=Math.max(m,c);
                c=0;
            }else{
                c+=1;
            }
        }
        return Math.max(c,m);
    }
}