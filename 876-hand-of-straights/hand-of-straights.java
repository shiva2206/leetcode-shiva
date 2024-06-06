class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i : hand){
            if(hm.containsKey(i)){
                hm.put(i,hm.get(i)+1);
            }else{
                hm.put(i,1);
                pq.add(i);
            }
        }

        while(pq.size()>0){
            int x = pq.peek();
            for(int i = 0;i<groupSize;i++){
                int y = x +i;
                if(!hm.containsKey(y)) return false;
                hm.put(y,hm.get(y)-1);
                if(hm.get(y)==0){
                    hm.remove(y);
                }
            }
            while(pq.size()>0 && !hm.containsKey(pq.peek())){
                pq.poll();
            }
        }

    return true;
    }
}