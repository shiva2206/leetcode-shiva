class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->{
            if(a[0]==b[0]) return a[1]-b[1];
            return a[0]-b[0];
        });
        for(int i = 0;i<nums.length;i++){
            pq.add(new int[]{nums[i],i});
        }

        for(int i = 0;i<k;i++){
            int[] res = pq.poll();
            nums[res[1]] = res[0]*multiplier;
            pq.add(new int[]{nums[res[1]],res[1]});
        }
        return nums;
    }
}