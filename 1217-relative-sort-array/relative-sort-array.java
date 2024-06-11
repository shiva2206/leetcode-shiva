class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i : arr1){
            hm.put(i,hm.getOrDefault(i,0)+1);
        }   

        int[] l = new int[arr1.length];
        int y = 0;
        for(int i : arr2){
            for(int j = 0;j<hm.get(i);j++){
                l[y] = i;
                y+=1;
            }
            hm.remove(i);
        }

        List<Integer> d = new ArrayList<>(hm.keySet());
        Collections.sort(d);
        for(int j : d){
            for(int i=0;i<hm.get(j);i++){
                l[y] = j;
                y+=1;
            }
        }
        return l;
    }
}