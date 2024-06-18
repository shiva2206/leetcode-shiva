class Solution {
    public int maxProfitAssignment(int[] diff, int[] prof, int[] work) {
        int[][] l = new int[diff.length][2];
        for(int i =0;i<diff.length;i++){
            l[i][0] = diff[i];
            l[i][1] = prof[i];
        }

        Arrays.sort(l,new Comparator<int[]>(){
            @Override
            public int compare(int[] a,int[] b){
                return Integer.compare(a[0],b[0]);
            }
        });

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a,b)->{
            return b-a;
        });

        int ans = 0,j=0;
        Arrays.sort(work);
        for(int i = 0;i<work.length;i++){
            while (j<l.length && work[i]>=l[j][0]){
                pq.add(l[j][1]);
                j+=1;
            }
            if(pq.size()>0)ans += pq.peek();
        }
        return ans;



    }
}