class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        HashSet<Integer> l = new HashSet<>();
        for(int i : days) l.add(i);

        int[] d = new int[days[days.length-1]+1];
        for(int i = 1;i<=days[days.length-1];i++){
            if(!l.contains(i)){
                d[i] = d[i-1];
            }else{
                int one = costs[0] + (i-1>=0 ? d[i-1] : 0);
                int seven = costs[1] + (i-7>=0 ? d[i-7] : 0);
                int thirty = costs[2] + (i-30>=0 ? d[i-30] : 0);
                d[i] = Math.min(one,seven);
                d[i] = Math.min(d[i],thirty);
            }
        }   
        return d[d.length-1];
    }
}