class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> res = new ArrayList<>();
        HashMap<Integer,Integer> d = new HashMap<>();
        for(int i : nums1){
            if(!d.containsKey(i)) d.put(i,0);
            d.put(i,d.get(i)+1);
        }   
        for(int i : nums2){
            if(d.containsKey(i) && d.get(i)>0){
                res.add(i);
                d.put(i,d.get(i)-1);
            }
        }
        int[] arr = new int[res.size()];
        for(int i = 0;i<res.size();i++){
            arr[i] = res.get(i);
        }
        return arr;
    }
}