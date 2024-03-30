class Solution {
    
    public int subarraysWithKDistinct(int[] nums, int k) {
        return dfs(nums,k) - dfs(nums,k-1);
    }

    public int dfs(int[] nums,int k){
        int i=0;
        int ans = 0;
        HashMap<Integer,Integer> d = new HashMap<>();
        for(int j=0;j<nums.length;j++){
            if (!d.containsKey(nums[j])){
                d.put(nums[j],0);
            }
            d.put(nums[j],d.get(nums[j])+1);
            while(d.size()>k){
                d.put(nums[i],d.get(nums[i]) -1);
                if(d.get(nums[i]) == 0){
                    d.remove(nums[i]);
                }
                i+=1;
            }
            ans += j-i+1;
        }
        return ans;
    }
}